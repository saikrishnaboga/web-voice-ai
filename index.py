import whisper


model = whisper.load_model("base")

result = model.transcribe("StandardRecording1.mp3", fp16=False)

with open("transcription.txt", "w") as f:
    f.write(result["text"])