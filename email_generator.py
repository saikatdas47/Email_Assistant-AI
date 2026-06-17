from groq import Groq
from config import GROQ_API_KEY, GENERATION_MODEL, TEMPERATURE, MAX_TOKENS
from prompts import (
    SYSTEM_PROMPT_A, USER_PROMPT_A_TEMPLATE,
    SYSTEM_PROMPT_B, USER_PROMPT_B_TEMPLATE
)

client = Groq(api_key=GROQ_API_KEY)

def generate_email_strategy_a(intent: str, facts: list, tone: str) -> str:
    """Strategy A: Role + Few-Shot + CoT using Groq"""
    facts_str = "\n".join([f"- {f}" for f in facts])
    user_prompt = USER_PROMPT_A_TEMPLATE.format(intent=intent, facts=facts_str, tone=tone)
    
    response = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_A},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content.strip()

def generate_email_strategy_b(intent: str, facts: list, tone: str) -> str:
    """Strategy B: Baseline Zero-Shot using Groq"""
    facts_str = "\n".join([f"- {f}" for f in facts])
    user_prompt = USER_PROMPT_B_TEMPLATE.format(intent=intent, facts=facts_str, tone=tone)
    
    response = client.chat.completions.create(
        model=GENERATION_MODEL,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_B},
            {"role": "user", "content": user_prompt}
        ],
        temperature=TEMPERATURE,
        max_tokens=MAX_TOKENS
    )
    return response.choices[0].message.content.strip()