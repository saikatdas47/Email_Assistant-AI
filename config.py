import os
from dotenv import load_dotenv

# স্ক্রিপ্ট যেখানে আছে সেখান থেকে .env ফাইল লোড করতে বাধ্য করা
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file. Please create .env with GROQ_API_KEY=...")

# সর্বশেষ Groq মডেল
GENERATION_MODEL = "qwen/qwen3-32b"
JUDGE_MODEL = "llama-3.3-70b-versatile"
TEMPERATURE = 0.7
MAX_TOKENS = 600