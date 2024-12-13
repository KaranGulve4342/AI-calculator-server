from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'https://ai-calculator-server-taupe.vercel.app'
PORT = '5173'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")