import pyaudio
import wave
import numpy as np

selected_input_device_index = None

# List available audio devices
def list_audio_devices():
    p = pyaudio.PyAudio()
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')
    
    print("")
    print("Available audio devices:")
    for i in range(0, numdevices):
        device_info = p.get_device_info_by_host_api_device_index(0, i)
        print(f"Device {i}: {device_info.get('name')}")
    
    print("")
    #selected_input_device_index = int(input("Enter the index of the input device: "))
    p.terminate()
    record_audio("output.wav", record_seconds=2, device_index=1)

# Record audio
def record_audio(output_filename, record_seconds=5, device_index=0):
    p = pyaudio.PyAudio()
    
    # Set up stream
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    input=True,
                    input_device_index=device_index,
                    frames_per_buffer=1024)
    
    print("Recording...")
    frames = []
    
    for _ in range(0, int(44100 / 1024 * record_seconds)):
        data = stream.read(1024)
        frames.append(data)
    
    print("Finished recording.")
    
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save the recorded data as a WAV file
    wf = wave.open(output_filename, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(44100)
    wf.writeframes(b''.join(frames))
    wf.close()

if __name__ == "__main__":
    list_audio_devices()
    #record_audio("output.wav", record_seconds=10, device_index=0)