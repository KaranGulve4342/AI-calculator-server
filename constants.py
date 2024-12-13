from dotenv import load_dotenv
import os
load_dotenv()

SERVER_URL = 'ai-calculator-server-taupe.vercel.app'
PORT = '8900'
ENV = 'dev'

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")