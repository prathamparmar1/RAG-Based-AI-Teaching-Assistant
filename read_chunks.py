import requests
import os
import json
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def create_embedding(text_list):
    #https://github.com/ollama/ollama/blob/main/docs/api.md    {multiple input}
    r = requests.post('http://localhost:11434/api/embed', json={
        'model': 'bge-m3',
        'input': text_list
    })

    embedding = r.json()['embeddings']
    return embedding

# embedding = create_embedding("the cat sat on the mat")
# print(embedding)


jsons = os.listdir('jsons')
my_dicts = []
chunk_id = 0
for json_file in jsons:
    with open (f"jsons/{json_file}") as f:
        content = json.load(f)
    print(f"Creating embedding for{json_file}")
    embeddings = create_embedding([c['text'] for c in content['chunks']])
    for i, chunk in enumerate(content['chunks']):
        chunk['chunk_id'] = chunk_id
        chunk['embedding'] = embeddings[i]
        chunk_id+=1
        my_dicts.append(chunk)
    break

# print(my_dicts)

df = pd.DataFrame.from_records(my_dicts)
# print(df)

incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]
# print(question_embedding)


#Find similarities of question_embedding to other embeddings
similarities = cosine_similarity(np.vstack(df['embedding'].values), [question_embedding]).flatten()
print(similarities)
max_similarity_index = similarities.argsort()[::-1][0:3]
print(max_similarity_index)

new_df = df.loc[max_similarity_index]
print(new_df[['title', 'number', 'text']])