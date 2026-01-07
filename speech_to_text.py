import whisper
import json

model= whisper.load_model("large-v2")

result= model.transcribe(audio="audios/output.mp3", 
                         language="hindi",
                         task = "translate",
                         word_timestamps=False)

# print(result['segments'])

chunks = []
for segment in result["segments"]:
    chunks.append({"start": segment['start'], "end": segment['end'], "text": segment['text']})
    
    
with open("output.json", "w") as f:
    json.dump(chunks,f) 