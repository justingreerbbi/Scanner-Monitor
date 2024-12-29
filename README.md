# Audio Scanner, Recorder, and Transcribe with Keyword Alerts

## Description

This application is designed to monitor and record audio from various sources, including live streams or direct line-in inputs. It leverages the power of OpenAI's Whisper model for like real-time transcription of the captured audio into text. Additionally, this project provides a feature to set custom keywords which, when detected in the transcribed text, trigger specific alerts to notify users.

**THIS SCRIPT IS SOLELY FOR DEVELOPMENT RIGHT NOW AND IS A WORK IN PROGRESS. TRY IT, FORK IT, PR UPDATES, ENJOY!**

## Features

- Monitor scanner feed from Online source <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Green_check.svg" width="15">
- Monitor scanner feed from line-in ( still in development )
- Record audio for later playback <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Green_check.svg" width="15">
- Transcribe audio to text using OpenAI Whisper <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Green_check.svg" width="15">
- Keyword Notifications <img src="https://upload.wikimedia.org/wikipedia/commons/0/03/Green_check.svg" width="15">

## Requirements

It is best to setup a virtual environment so you don't muddy your core Python libraries up.

-   Recommended Python Version: **3.11** (https://www.python.org/downloads/)
-   ffmpeg

Install ffmpeg using choco or brew.

```
brew install ffmpeg
```

**Note:** Python version 3.11 or newer is not supported by OpenAI Whisper, thus not support by this application if you choose to use transcribing.

## Installation

1. Clone the repository:
    ```
    git clone https://github.com/justingreerbbi/Scanner-Monitor.git
    ```
2. Navigate to the project directory:

    ```
    cd Scanner-Monitor
    ```

## Usage

1. Run Only Once... Requirements

    ```
    pip install -r requirements.txt
    ```

2. Start the application:

    ```
    python listen.py
    ```

    **Note**: On your first run with OpenAI Whisper, you will need internet connection. The application will download the model and automatically proceed to scanning, recording and transcribing.

3. Follow the on-screen instructions. For demo purposes, use the stream url "https://broadcastify.cdnstream1.com/13705".

### Supported Config Options

| Option                | Description                                      | Default Value          |
|-----------------------|--------------------------------------------------|------------------------|
| KEYWORDS              | List of keywords to trigger alerts               |                        |
| RECORD_SECONDS        | Duration after end of audio to record in seconds | `2`                    |
| OUTPUT_DIRECTORY      | Directory to save recorded audio and transcripts | `./output`             |
| TRANSCRIBE_ENABLED    | Enable or disable transcription                  | `True`                 |
| WHISPER_MODEL         | Whisper model to use for transcription           | `base`                 |
| SHOW_RECOGNIZED_TEXT  | Display recognized text in the console           | `True`                 |

## Config File

The config file can be used to for easier management.

-   Keywords: Keywords are separated by a space. Single keywords are only supported currently.

I do plan on completing the config file fully. For now, only keywords are supported.

## Contributing

There is a long list of possibilities for this project. Since the project is just a proof of concept, there is limited support but all feedback and help is welcome. A PR can be submitted with all bug fixes, additional features, and optimizations.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or suggestions, please open an issue.

## Todos

- [ ] Add support for line-in audio.
- [ ] Add better options for ease of use.
- [x] Archive Structure of audio and text files respectively.
- [ ] Cleanup function for older content.
- [ ] Compression of archive files for storage.
- [ ] Build wrapper for python script.

#### Attribution
- gmaxwell, Public domain, via Wikimedia Commons
