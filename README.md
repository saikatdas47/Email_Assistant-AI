# Email Generation Assistant (Groq Edition)

## Setup
1. Clone the repo.
2. Create virtual env and install: pip install groq python-dotenv pandas
3. Create `.env` with `GROQ_API_KEY=...`.

## Run python main.py


## Models Used
- Generation: `mixtral-8x7b-32768` (fast & capable)
- Judge: `llama3-70b-8192` (for high-quality evaluation)

## Output
- JSON and CSV reports with 3 custom metrics.
- Console shows comparative analysis.

## Note
All prompts and evaluation logic are identical to the OpenAI version, just the backend is swapped with Groq for faster inference and free-tier benefits.