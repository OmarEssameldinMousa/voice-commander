# 🗣️ Whisper Voice Command System

A simple Python-based voice command system using [OpenAI's Whisper](https://github.com/openai/whisper) model for transcription and command recognition.

This project records audio through the microphone, transcribes it locally using Whisper, and triggers simple actions like `GO FORWARD`, `TURN LEFT`, etc., based on voice input.

---

## 📦 Features

- 🎙️ Record audio from microphone
- 🧠 Transcribe speech using Whisper (`base` or `tiny` models)
- 🧾 Match common control phrases like:
  - "go forward"
  - "turn left"
  - "stop"
  - "turn right"
- 💡 Easy to extend with more commands

---

## 🛠️ Setup

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/whisper-voice-command.git
cd whisper-voice-command
````

### 2. Create a Virtual Environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install git+https://github.com/openai/whisper.git
pip install sounddevice scipy
```

Also install system-level dependencies for audio:

```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev
```

---

## 🚀 Run the App

```bash
python main.py
```

You’ll be prompted to speak a command. The script will:

1. Record 5 seconds of audio
2. Transcribe it using Whisper
3. Match keywords and print a simulated control response

---

## 🔧 Example Output

```
Recording for 5 seconds...
Audio saved to command.wav
Transcribed: go forward now
COMMAND: GO FORWARD
```

---

## 🧠 How It Works

* Uses `sounddevice` to record `.wav` audio
* Transcribes using Whisper’s local PyTorch model
* Parses command from transcription with basic string matching

---

## 📌 Notes

* For faster inference, replace `base` with `tiny`:

```python
model = whisper.load_model("tiny")
```

* You can modify `process_command()` in `main.py` to handle more commands.

---

## 🔗 Related Projects

* [OpenAI Whisper GitHub](https://github.com/openai/whisper)
* [Whisper.cpp (C++ inference)](https://github.com/ggerganov/whisper.cpp)
* [Faster Whisper (CTC-based)](https://github.com/guillaumekln/faster-whisper)


