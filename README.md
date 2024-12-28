 # Scanner Monitor, Recorder, and Transcriber #

## Description
Scanner Monitor, Recorder, and Transcriber is a python tool designed to monitor, record, and transcribe scanner audio. The script can monitor a scan feed from Broadcastify or any other provider (even a local server). On detection of audio output, the script will start recording the audio which is then stored and transcribed using Google Speech to Text.

Scanner audio can be a bit on teh harsh side as far as quality, but the system does its best to transcribe the contents. Keywords can be used to trigger and event like a tone, email, or a popup alert to notify you when something specific is found.

## Features
- Monitor scanner feed from Online source
- Monitor scanner feed from line-in
- Record audio for later playback
- Transcribe audio to text
- Keyword Notifications

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/Scanner-Monitor.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Scanner-Monitor
    ```

4. Install the required Python packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Start the application:
    ```sh
    python listen.py
    ```
2. Follow the on-screen instructions.

## Contributing
There is a long list of possibilities for this project. Since the project is just a proof of concept, there is limited support but all feedback and help is welcome. A PR can be submitted with all bug fixes, additional features, and optimizations. 

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or suggestions, please open an issue or contact the repository owner.

## Todos
- Add support for line-in audio.
- Add better options for ease of use.
- Ability to pipe in audio with other Speech to Text API's.
- Archive Structure of audio and text files respectively.
- Cleanup function for older scripts.
- Compression of archive files for storage.

