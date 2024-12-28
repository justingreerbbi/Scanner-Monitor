import numpy as np
import requests
from pydub import AudioSegment
from pydub.playback import play
from speech_recognition import Recognizer, AudioFile
import io
import wave
import os

# Constants
CHUNK = 1024 # Audio chunk size
RECORD_SECONDS = 5
THRESHOLD = 1  # Audio level threshold; adjust as needed
WAVE_OUTPUT_FILENAME = "./output.wav"
URL = "https://broadcastify.cdnstream1.com/13705"

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
                    print("Recording started...")
                    recording = True
                    frames = [segment]
                elif rms <= THRESHOLD and recording:
                    print("Recording stopped.")
                    recording = False
                    
                    # Combine recorded frames
                    combined = sum(frames)
                    
                    # Save audio to a .wav file
                    combined.export(WAVE_OUTPUT_FILENAME, format="wav")
                    
                    # Convert audio to text
                    recognizer = Recognizer()
                    with AudioFile(WAVE_OUTPUT_FILENAME) as source:
                        audio = recognizer.record(source)
                        try:
                            text = recognizer.recognize_google(audio)
                            print(f"Recognized text: {text}")
                            
                            # Save the text to a file
                            with open("recognized_text.txt", "a") as text_file:
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
        combined.export(WAVE_OUTPUT_FILENAME, format="wav")

print("Finished monitoring and recording.")