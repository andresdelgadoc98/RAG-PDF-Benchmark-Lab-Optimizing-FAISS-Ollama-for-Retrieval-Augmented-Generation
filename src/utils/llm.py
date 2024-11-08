import ollama
import os
from dotenv import load_dotenv
load_dotenv()
model_llm = os.getenv("MODEL_LLM")

def get_chat_response(prompt : str ,format='none') -> str:
    chat_args = {
        'model': model_llm,
        'format': format,
        'messages': [{'role': 'user', 'content': prompt}],
        'stream': True,
    }

    stream = ollama.chat(**chat_args)

    message_content = ""
    for chunk in stream:
        message_content += chunk['message']['content']

    return message_content