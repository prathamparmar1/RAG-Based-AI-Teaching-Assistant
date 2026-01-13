# How to use this RAG AI Teaching Assistant on your own data

## Step 1 - Collect your videos
Move all your videos files to the videos folder

## Step 2 - Convert to mp3
Convert all the video files to mp3 by running process_vid_to_aud

## Step 3 - Convert mp3 to JSON
Convert all the mp3 files to json by running mp3_to_json

## Step 4 - COnvert the json files to Vectors
Use the file proprocess_json to convert the json files to a dataframe with Embeddings and save it as a joblib pickle

## Step 5 - Prompt generation and feeding to LLM 
Read the joblib file and load it into the memory. Then create a relavent promptas per the user query and feed it to the LLM. Use file process_incoming for this.
