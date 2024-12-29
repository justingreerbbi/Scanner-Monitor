 # Scanner Monitor, Recorder, and Transcriber #

## Description
Scanner Monitor, Recorder, and Transcriber is a python tool designed to monitor, record, and transcribe scanner audio. The script can monitor a scan feed from Broadcastify or any other provider (even a local server). On detection of audio output, the script will start recording the audio which is then stored and transcribed using Google Speech to Text.

Scanner audio can be a bit on the harsh side as far as quality, but the system does its best to transcribe the contents. Keywords can be used to trigger and event like a tone, email, or a popup alert to notify you when something specific is found.

**THIS SCRIPT IS SOLELY FOR DEVELOPMENT RIGHT NOW AND IS A WORK IN PROGRESS. TRY IT, FORK IT, PR UPDATES, ENJOY!**

## Features
- Monitor scanner feed from Online source
- Monitor scanner feed from line-in
- Record audio for later playback
- Transcribe audio to text (Google or OpenAI Whisper)
- Keyword Notifications

## Requirements
For running Python versions, it is best top setup a virtual interpreter so you don't muddy your core Python libraries up.

- Python 3.13.0 Works for the listener and Google translate.
- Python 3.11.9 is required to to run the openai-whisper code and listener.

## Installation
The script does depend on **FFMPEG** to be installed. Be sure this is installed.

1. Clone the repository:
    ```sh
    git clone https://github.com/justingreerbbi/Scanner-Monitor.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Scanner-Monitor
    ```

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```
OR download the code directly from the repo.

## Usage

### Using Google Voice Translate Option
**Note:** Google Translate requires internet connection in order to translate.

1. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ``` 
2. Start the application:
    ```sh
    python listen.py
    ```
3. Follow the on-screen instructions. For demo purposes, use the stream url "https://broadcastify.cdnstream1.com/13705".

#### Supported Config Options
- KEYWORDS
- RECORD_SECONDS
- OUTPUT_DIRECTORY
- TRANSCRIBE_ENABLED

### Using OpenAI Whisper Translate Option
Using OpenAI Whisper does not require an internet connection, is more accurate, but does take more time to process.

1. Run Only Once... Requirements 
    ```sh
    pip install -r requirements_whisper.txt
    ```

2. Start the application:

    ```sh
    python listen-whisper.py
    ```
    **Note**: On your first run with whisper, you will need internet connection. The application will download the model and automatically proceed to scanner, recording and transcribing.
    
3. Follow the on-screen instructions. For demo purposes, use the stream url "https://broadcastify.cdnstream1.com/13705".

#### Supported Config Options
- KEYWORDS
- RECORD_SECONDS
- OUTPUT_DIRECTORY
- TRANSCRIBE_ENABLED
- WHISPER_MODEL

## Config File
The config file can be used to for easier management. 

- Keywords: Keywords are separated by a space. Single keywords are only supported currently.

I do plan on completing the config file fully. For now, only keywords are supported.

## Contributing
There is a long list of possibilities for this project. Since the project is just a proof of concept, there is limited support but all feedback and help is welcome. A PR can be submitted with all bug fixes, additional features, and optimizations. 

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue.

## Todos
- Add support for line-in audio.
- Add better options for ease of use.
- Ability to pipe in audio with other Speech to Text API's.
- Archive Structure of audio and text files respectively.
- Cleanup function for older scripts.
- Compression of archive files for storage.
- Build wrapper for python script. 
- Add config options into both google and whisper applications.
