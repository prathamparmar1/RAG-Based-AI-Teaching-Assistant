import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests
from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()
client = genai.Client()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")

def create_embedding(text_list):
    #https://github.com/ollama/ollama/blob/main/docs/api.md    {multiple input}
    r = requests.post('http://localhost:11434/api/embed', json={
        'model': 'bge-m3',
        'input': text_list
    })

    embedding = r.json()['embeddings']
    return embedding

def inference(prompt):
    response = client.models.generate_content(
    model="gemini-2.5-flash", contents=prompt
    )
    return response

df = joblib.load('embeddings.joblib')

incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]

#Find similarities of question_embedding to other embeddings
similarities = cosine_similarity(np.vstack(df['embedding'].values), [question_embedding]).flatten()
top_results = 5
max_similarity_index = similarities.argsort()[::-1][0:top_results]
new_df = df.loc[max_similarity_index]

prompt  = f'''I am teaching web development sigma web development course. 
Here are video subtitle chunks containing video title, video number, start time(in seconds), 
end time(in seconds), the text at that time: "{new_df[['title', 'number', 'start', 'end', 'text']].to_json(orient="records")}".
-----------------
"{incoming_query}"
User asked this question related to the video chunks, 
you have to answer in human way(don't mention the above format, it was just for you)that
where and how much content is taught where(in which video and at what timestamp)
and guide the user to go to that particular video. If user asks unrelated question
, tell him that you can only answer question to the course'''

# for index, item in new_df.iterrows():
#     print(index, item['title'], item['number'], item['text'], item['start'], item['end'])
with open('prompt.txt', "w") as f:
    f.write(prompt)
    
response = inference(prompt)
r = str(response).split('"""')[1].split('"""')[0]
with open('response.txt', "w") as res:
    res.write(r)
print(r)