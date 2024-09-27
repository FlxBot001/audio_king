from pydub import AudioSegment
import os

def process_audio_file(filepath):
    # Convert to MP3 if needed
    base, ext = os.path.splitext(filepath)
    if ext != '.mp3':
        audio = AudioSegment.from_file(filepath)
        output_path = f"{base}.mp3"
        audio.export(output_path, format='mp3')
