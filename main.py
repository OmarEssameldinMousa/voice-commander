import sounddevice as sd
from scipy.io.wavfile import write
import whisper


def record_audio(filename="command.wav", duration=5, fs=44100):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    write(filename, fs, audio)
    print(f"Audio saved to {filename}")
    return filename


def transcribe_audio(model, filename):
    result = model.transcribe(filename)
    text = result["text"].strip().lower()
    print(f"Transcribed: {text}")
    return text


def process_command(text):
    if "forward" in text:
        print("COMMAND: GO FORWARD")
    elif "stop" in text:
        print("COMMAND: STOP")
    elif "left" in text:
        print("COMMAND: TURN LEFT")
    elif "right" in text:
        print("COMMAND: TURN RIGHT")
    else:
        print("COMMAND: Unrecognized")


if __name__ == "__main__":
    model = whisper.load_model("base") 
    filename = record_audio()
    transcription = transcribe_audio(model, filename)
    process_command(transcription)
