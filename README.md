Here's a detailed `README.md` file for the provided code:

---

# Whisper MP3 Transcription Script

This script automates the process of transcribing MP3 audio files into text using OpenAI's Whisper model. It reads MP3 files from a designated directory, transcribes them into text, and saves the results as markdown files in organized folders for each episode.

## Features

- Automatically scans a directory for MP3 files.
- Uses OpenAI's Whisper model for transcription.
- Creates organized folders for each episode and saves the transcript as a markdown file.
- Supports various Whisper model types (`base`, `small`, `medium`, `large`) based on the user's needs.

## Requirements

- Python 3.8+
- [OpenAI Whisper](https://github.com/openai/whisper)
- FFmpeg (required by Whisper for audio processing)

## Installation

1. Clone this repository and navigate to the project directory:

   ```bash
   git clone https://github.com/discoposse/whisper-bulk-transcriber
   cd whisper-bulk-transcriber
   ```

2. Install the required Python packages:

   ```bash
   pip install whisper
   ```

3. Ensure FFmpeg is installed on your system. You can download it from [FFmpeg's official website](https://ffmpeg.org/download.html).

## Directory Structure

The script expects the following folder structure:

```
/project_directory
│
├── mp3_files/         # Place your MP3 files here
│   ├── episode1.mp3
│   └── episode2.mp3
│
└── episodes/          # Output folder for transcriptions (created automatically)
    ├── episode1/
    │   └── episode1.md
    └── episode2/
        └── episode2.md
```

- **mp3_files/**: Place all your MP3 files in this directory.
- **episodes/**: This directory will be created automatically, and each episode will have its own folder containing the transcription in markdown format.

## Usage

1. Place your MP3 files into the `mp3_files` directory.
2. Run the script:

   ```bash
   python transcribe.py
   ```

3. The script will automatically process each MP3 file, create a folder for each episode, and save the transcription in a markdown file.

## Changing the Model

The script uses the "base" model by default, but you can change the model type depending on your accuracy and performance needs. Available model types:

- `base`
- `small`
- `medium`
- `large`

To change the model, modify this line in the script:

```python
model = whisper.load_model("base")
```

For example, to use the `medium` model, update it to:

```python
model = whisper.load_model("medium")
```

## Troubleshooting

- **Whisper Installation Issues**: Make sure you have installed Whisper correctly via pip and that all dependencies, including FFmpeg, are available in your system's PATH.
- **File Not Found Errors**: Ensure the `mp3_files` directory exists and contains your MP3 files.

## Contributing

Feel free to submit issues or pull requests to improve this script.

## License

This project is licensed under the MIT License.
