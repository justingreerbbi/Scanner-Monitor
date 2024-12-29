import whisper
import numpy as np
import requests
from pydub import AudioSegment
from pydub.playback import play
from pydub.generators import Sine
import io
import os
from datetime import datetime
import warnings

print("")
print("#######################################################")
print("# Scanner, Recorder, and Transcribed By OpenAI Whisper")
print("# Author: Justin Greer justingreer750@gmail.com")
print("# Version: 1.0")
print("# License: MIT")
print("#")
print("# Enjoy! Please report any issues.")
print("#######################################################")

# Warning suppression since there is a lot going on.
warnings.filterwarnings("ignore")

# Load the Whisper Model
# tiny, base, small, medium, large, turbo
transcribe_model = whisper.load_model('base')

## Define the keywords variable as an empty list
KEYWORDS = []

# load the config.txt file and parse the allowed values
if os.path.exists('./config.txt'):
    with open('./config.txt') as f:
        lines = f.readlines()
        for line in lines:
            if line.startswith('KEYWORDS'):
                KEYWORDS = line.split('=')[1].strip()
                KEYWORDS = KEYWORDS.split(' ')
                print("")
                print(f"Alert on Keywords: {KEYWORDS}")

# Constants
CHUNK = 1024 * 8  # Audio chunk size
RECORD_SECONDS = 2
THRESHOLD = 1  # Audio level threshold; adjust as needed
OUTPUT_DIRECTORY = "./recordings"

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)

# Ask the user for the URL
# Testing URL: https://broadcastify.cdnstream1.com/13705
print("")
URL = input("Enter the URL of the audio stream: ")
print("")

# Ensure the URL is valid, if not, bail.
if not URL:
    print("No URL provided. Exiting.")
    exit()

print('')
print("* Start monitoring audio")

frames = []
recording = False

try:
    with requests.get(URL, stream=True) as response:
        response.raise_for_status()
        audio_stream = io.BytesIO()
        
        for chunk in response.iter_content(chunk_size=CHUNK):
            if chunk:  # filter out keep-alive new chunks
                audio_stream.write(chunk)
                audio_stream.seek(0)
                
                # Load audio chunk into AudioSegment
                segment = AudioSegment.from_file(audio_stream, format="mp3")  # Assuming MP3, adjust if it's another format
                audio_stream = io.BytesIO()  # Reset for next chunk
                
                # Convert to numpy array for RMS calculation
                samples = np.array(segment.get_array_of_samples())
                # Convert samples to -1 to 1 range if not already
                if segment.sample_width == 2:
                    samples = samples.astype(np.int16) / 32768.0  # Normalize for 16-bit audio
                elif segment.sample_width == 4:
                    samples = samples.astype(np.int32) / 2147483648.0  # Normalize for 32-bit audio
                
                # Calculate RMS of audio data
                rms = np.sqrt(np.mean(samples**2))

                # Convert RMS to whole number
                rms = int(rms * 1000)
                
                #print(f"RMS: {rms}")
                if rms > THRESHOLD and not recording:
                    #print("Recording started...")
                    recording = True
                    frames = [segment]
                elif rms <= THRESHOLD and recording:
                    #print("Recording stopped.")
                    recording = False

                    # Create a directory for today's date if it doesn't exist
                    today_date = datetime.now().strftime('%Y%m%d')
                    TODAY_DIRECTORY = os.path.join(OUTPUT_DIRECTORY, today_date)
                    if not os.path.exists(TODAY_DIRECTORY):
                        os.makedirs(TODAY_DIRECTORY)
                    
                    # Create a directory for the current hour if it doesn't exist
                    current_hour = datetime.now().strftime('%H')
                    HOUR_DIRECTORY = os.path.join(TODAY_DIRECTORY, current_hour)
                    if not os.path.exists(HOUR_DIRECTORY):
                        os.makedirs(HOUR_DIRECTORY)

                    # Configuration for the specific recording.
                    RECORDED_DATE_TIME = datetime.now().strftime('%Y%m%d_%H%M%S')
                    RECORDED_OUTPUT_FILENAME = f"{HOUR_DIRECTORY}/recording_{RECORDED_DATE_TIME}.mp3"
                    
                    # Combine recorded frames
                    combined = sum(frames)
                    
                    # Save audio to a .mp3 file
                    combined.export(RECORDED_OUTPUT_FILENAME, format="mp3")

                    # Play the recorded audio
                    play(combined)

                    try:
                        text = transcribe_model.transcribe(RECORDED_OUTPUT_FILENAME)
                        text = text["text"]
                        print(f"Recognized text: {text}")

                        for keyword in KEYWORDS:
                            if keyword in text:
                                print(f"Keyword '{keyword}' found in text: {text}. Trigger Event!")
                                
                                # Open a new window with text containing the keyword found
                                #webbrowser.open_new_tab(f"data:text/plain,{text}")
                                tone = Sine(1000.0).to_audio_segment(duration=2000)  # 1000 Hz is the frequency of the alarm tone
                                play(tone)

                        # Save the text to a file
                        with open(f"{HOUR_DIRECTORY}/recording_text_{RECORDED_DATE_TIME}.txt", "w") as text_file:
                            text_file.write(text + "\n")

                    except Exception as e:
                        print(f"Could not recognize speech: {e}")
                   
                    # Clear frames for the next recording
                    frames = []
                elif recording:
                    frames.append(segment)

except requests.RequestException as e:
    print(f"Failed to connect to the stream: {e}")
except KeyboardInterrupt:
    print("\nInterrupted by user")

finally:
    # Ensure the last recording is saved if interrupted while recording
    if frames:
        combined = sum(frames)
        combined.export(RECORDED_OUTPUT_FILENAME, format="wav")

print("Finished monitoring and recording.")