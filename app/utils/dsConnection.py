from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv('DEEPSEEK_KEY'),base_url=os.getenv('DEEPSEEK_URL'))    