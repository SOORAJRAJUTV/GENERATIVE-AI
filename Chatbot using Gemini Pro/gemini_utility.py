import os
import json

import google.generativeai as genai
from google.generativeai import GenerativeModel



working_directory = os.path.dirname(os.path.abspath(__file__))

config_file_path = f"{working_directory}/config.json"
config_data = json.load(open(config_file_path))

#configuring google.generativeai with api key
GOOGLE_API_KEY = config_data["GOOGLE_API_KEY"]
genai.configure(api_key=GOOGLE_API_KEY)


# function to load gemini-pro-model for chatbot
def load_gemini_pro_model():
    gemini_pro_model = GenerativeModel("gemini-pro")
    return gemini_pro_model


# function for image captioning
def gemini_pro_vision_response( prompt,image ):
    gemini_pro_vision_model = GenerativeModel("gemini-1.5-flash") #gemini-pro-vision model has been deprecated
    response = gemini_pro_vision_model.generate_content([prompt,image])
    result = response.text
    return result


def embedding_model_response(input_text):
    embedding_model = "models/embedding-001"
    embedding = genai.embed_content(model = embedding_model,
                                    content = input_text,
                                    task_type = "retrieval_document") # task_type = "retrieval_document"
    embedding_list = embedding["embedding"] #since the result is in the form of a dict with key name as "embedding"
    return embedding_list



# function to get response from gemini-pro-llm

def gemini_pro_response(user_prompt):
    gemini_pro_model = GenerativeModel("gemini-pro")
    response = gemini_pro_model.generate_content(user_prompt)
    result = response.text
    return result