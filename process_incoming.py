import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import joblib
import requests

def create_embedding(text_list):
    #https://github.com/ollama/ollama/blob/main/docs/api.md    {multiple input}
    r = requests.post('http://localhost:11434/api/embed', json={
        'model': 'bge-m3',
        'input': text_list
    })

    embedding = r.json()['embeddings']
    return embedding


df = joblib.load('embeddings.joblib')

incoming_query = input("Ask a Question: ")
question_embedding = create_embedding([incoming_query])[0]
# print(question_embedding)


#Find similarities of question_embedding to other embeddings
similarities = cosine_similarity(np.vstack(df['embedding'].values), [question_embedding]).flatten()
# print(similarities)
top_results = 5
max_similarity_index = similarities.argsort()[::-1][0:top_results]
# print(max_similarity_index)

new_df = df.loc[max_similarity_index]
# print(new_df[['title', 'number', 'text']])

prompt  = f'''I am teaching web development sigma web development course. 
Here are video subtitle chunks containing video title, video number, start time(in seconds), 
end time(in seconds), the text at that time: "{new_df[['title', 'number', 'start', 'end', 'text']].to_json()}".
-----------------
"{incoming_query}"
User asked this question related to the video chunks, 
you have to answer where and how much content is taught where(in which video and at what timestamp)
and guide the user to go to that particular video. If user asks unrelated question
, tell him that you can only answer question to the course'''

# for index, item in new_df.iterrows():
#     print(index, item['title'], item['number'], item['text'], item['start'], item['end'])
with open('prompt.txt', "w") as f:
    f.write(prompt)