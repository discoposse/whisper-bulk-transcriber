import os
import whisper

# Define the paths
base_dir = os.path.dirname(os.path.abspath(__file__))
mp3_dir = os.path.join(base_dir, 'mp3_files')
episodes_dir = os.path.join(base_dir, 'episodes')

# Create the 'episodes' folder if it doesn't exist
os.makedirs(episodes_dir, exist_ok=True)

# Load the Whisper model
model = whisper.load_model("base")  # You can change "base" to another model type like "small", "medium", "large" depending on your needs

# Iterate over each MP3 file in the mp3_files directory
for file_name in os.listdir(mp3_dir):
    if file_name.endswith('.mp3'):
        # Define paths and output names
        mp3_path = os.path.join(mp3_dir, file_name)
        episode_title = os.path.splitext(file_name)[0]
        episode_folder = os.path.join(episodes_dir, episode_title)
        transcript_path = os.path.join(episode_folder, f"{episode_title}.md")

        # Create a folder for the episode if it doesn't exist
        os.makedirs(episode_folder, exist_ok=True)

        # Transcribe the audio file
        print(f"Transcribing: {file_name}...")
        result = model.transcribe(mp3_path)

        # Save the transcript to a markdown file
        with open(transcript_path, 'w') as f:
            f.write(f"# {episode_title}\n\n")
            f.write(result['text'])

        print(f"Transcript saved: {transcript_path}")

print("All transcriptions completed.")
