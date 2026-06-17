import json
import re
from groq import Groq
from config import GROQ_API_KEY, JUDGE_MODEL
from prompts import JUDGE_SYSTEM_PROMPT, JUDGE_USER_TEMPLATE

client = Groq(api_key=GROQ_API_KEY)

def evaluate_email(generated_email: str, facts: list, tone: str) -> dict:
    """
    Groq-কে জাজ বানিয়ে ৩টি মেট্রিকের স্কোর বের করি।
    Groq JSON মোড সাপোর্ট করে না, তাই আমরা টেক্সট পার্স করব।
    """
    facts_str = "\n".join([f"- {f}" for f in facts])
    
    user_prompt = JUDGE_USER_TEMPLATE.format(
        tone=tone,
        facts=facts_str,
        generated_email=generated_email
    )
    
    try:
        response = client.chat.completions.create(
            model=JUDGE_MODEL,
            messages=[
                {"role": "system", "content": JUDGE_SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.2,
            max_tokens=200
        )
        raw_output = response.choices[0].message.content.strip()
        
        
        json_match = re.search(r'\{.*\}', raw_output, re.DOTALL)
        if json_match:
            result = json.loads(json_match.group())
        else:
            # যদি JSON না পাই, তাহলে ডিফল্ট স্কোর (এড়িয়ে যাওয়া)
            result = {"factual_coverage": 5.0, "tone_adherence": 5.0, "quality_structure": 5.0}
        
        # নিশ্চিত করা
        for key in ["factual_coverage", "tone_adherence", "quality_structure"]:
            if key not in result:
                result[key] = 5.0
        return result
    except Exception as e:
        print(f"Evaluation failed: {e}")
        return {"factual_coverage": 0.0, "tone_adherence": 0.0, "quality_structure": 0.0}