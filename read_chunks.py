import requests
import os
import json

def create_embedding(text):
    r = requests.post('http://localhost:11434/api/embeddings', json={
        'model': 'bge-m3',
        'prompt': text
    })

    embedding = r.json()['embedding']
    return embedding


jsons = os.listdir('jsons')

for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content = json.load(f)
    for chunk in content['chunks']:
        print(chunk)