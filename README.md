# Email Generation Assistant (Groq Edition)
# How to Reproduce (Step-by-Step Instructions) - Setup & Installation
## Setup
1. Clone the repo.
2. Create virtual env and install: pip install groq python-dotenv pandas
3. Create `.env` with `GROQ_API_KEY=...`.

## Run python main.py


## Models Used
- Generation: `mixtral-8x7b-32768` (fast & capable)
- Judge: `llama3-70b-8192` (for high-quality evaluation)

## Expected Output
- **Console**: Prints progress for 10 scenarios, average scores, and a comparative analysis.
- **Files Generated**:
  - `evaluation_report_<timestamp>.json` (Raw metric scores)
  - `evaluation_report_<timestamp>.csv` (Excel-friendly table)

## Note
All prompts and evaluation logic are identical to the OpenAI version, just the backend is swapped with Groq for faster inference and free-tier benefits.



Here is the **complete wrap-up** of your project. I have broken down everything you did, why you did it, your actual results, exact steps to reproduce, evidence requirements (screenshots), and the final GitHub `README.md` template with proper file structure.

---

## 1. What I Have Done (Project Summary)

I built a fully functional **Email Generation Assistant** that uses Groq's fast LLM API. I tested **two different prompting strategies** against 10 unique scenarios and evaluated them using **3 custom metrics** via an LLM-as-a-Judge.

**Actions:**
1. Created a Python project with 8 modular files (`config.py`, `prompts.py`, `test_data.py`, `email_generator.py`, `evaluator.py`, `report.py`, `main.py`, `app.py` optional).
2. Wrote **10 test scenarios** (Intent + Facts + Tone) with Human Reference Emails.
3. Implemented **Strategy A (Advanced)**: System prompt with *Role-Playing*, *2 Few-Shot examples*, and *4-step Chain-of-Thought*.
4. Implemented **Strategy B (Baseline)**: Simple Zero-Shot system prompt ("Write a professional email").
5. Connected to **Groq API** using `qwen/qwen3-32b` for generation and `llama-3.3-70b-versatile` as the Judge.
6. Defined **3 custom metrics**:
   - **Factual Coverage** (Did it include all bullet points?)
   - **Tone Adherence** (Did it match formal/casual/urgent/empathetic?)
   - **Quality/Structure** (Is it grammatically correct, concise, and well-formatted?)
7. Ran the evaluation pipeline, generating `JSON` and `CSV` reports.
8. Output a comparative analysis to the console.

---

## 2. Why I Did This (Rationale)

| Decision | Why? |
| :--- | :--- |
| **Used Groq instead of OpenAI** | Groq is **100x faster** for inference, has a generous free tier, and is OpenAI-compatible. Ideal for quick prototyping. |
| **Used Strategy A (Advanced)** | To prove that *advanced prompting* (Role + Few-Shot + CoT) adds value. Theoretically, it forces the model to "think" step-by-step and follow strict formatting. |
| **Used Strategy B (Baseline)** | To establish a *control* group. Without a baseline, you cannot prove your prompt engineering works. |
| **Used LLM-as-a-Judge** | Manual scoring is subjective and slow. Using a strong, second LLM (`llama-3.3-70b`) as a judge ensures **consistent, repeatable, and objective** metric scoring across 10 scenarios. |
| **Created 3 Custom Metrics** | General metrics (like BLEU or ROUGE) don't work for creative text like emails. Factual Coverage, Tone, and Structure are the **three most important qualities** of a professional email. |
| **Generated JSON & CSV** | JSON is machine-readable, CSV is human-readable (Excel). Providing both makes the evaluation transparent. |

---

## 3. Results (My Actual Data)

> **Note:** This is based on my actual run (`evaluation_report`).

### Overall Average Scores:
| Strategy | Factual Coverage | Tone Adherence | Quality/Structure | **Overall** |
| :--- | :---: | :---: | :---: | :---: |
| **A (Advanced)** | 9.40 | 9.20 | 9.00 | 9.20 |
| **B (Baseline)** | **9.50** | 9.10 | **9.20** | **🏆 9.27** |

To make your submission bulletproof, take the following screenshots:
<img width="1200" height="" alt="ResultTerminalSSprove" src="https://github.com/user-attachments/assets/53fe2e7b-fd82-4b49-915f-c60d2844353d" />

### Key Insights:
- **Strategy B (Baseline) won** by a tiny margin (0.07 points).
- **Why Strategy A lost**: In some scenarios (like Scenarios 3 & 6), the "advanced" prompt caused the model to overthink. It focused too much on being "empathetic" and forgot to mention specific facts (e.g., the *20% revenue increase* in Scenario 6).
- **Recommendation**: For production, Ship **Strategy B** immediately (cheaper, faster, marginally better). Keep **Strategy A** as an optional "Expert Mode" for formal legal/HR emails, as it performed flawlessly there (Scenario 9: 10/10/10).

---



```
email_assistant/
├── .env                    # Environment variables (GROQ_API_KEY)
├── .gitignore              # Ignore venv, .env, pycache
├── README.md               # This file
├── config.py               # API keys, model configs
├── prompts.py              # Strategy A (Advanced) & Strategy B (Baseline) prompts
├── test_data.py            # 10 test scenarios + Human Reference Emails
├── email_generator.py      # Groq API calls for both strategies
├── evaluator.py            # LLM-as-Judge (3 custom metrics)
├── report.py               # JSON & CSV report generation
├── main.py                 # Orchestrates the entire pipeline
└── app.py                  # (Optional) Streamlit UI for live demo
```


## 🔬 Evaluation Metrics (LLM-as-Judge)

| Metric | Focus | Scoring Logic (0-10) |
| :--- | :--- | :--- |
| **Factual Coverage** | Fact Recall | 10 = All input bullet points are explicitly mentioned. |
| **Tone Adherence** | Style Accuracy | 10 = Perfectly matches requested tone (Formal/Casual/Urgent/Empathetic). |
| **Quality/Structure** | Professionalism | 10 = Flawless grammar, flow, subject line, greeting, and sign-off. |

## 🧪 Tested Strategies

- **Strategy A (Advanced)**: Role-Playing + 2 Few-Shot Examples + 4-step Chain-of-Thought.
- **Strategy B (Baseline)**: Simple Zero-Shot instruction ("Write a professional email").

## 📊 Results Summary

| Strategy | Factual Coverage | Tone Adherence | Quality/Structure | **Overall** |
| :--- | :---: | :---: | :---: | :---: |
| **A (Advanced)** | 9.40 | 9.20 | 9.00 | 9.20 |
| **B (Baseline)** | **9.50** | 9.10 | **9.20** | **🏆 9.27** |

**Conclusion**: Strategy B (Baseline) slightly outperformed Advanced prompting for this specific dataset. However, Strategy A is more robust for highly formal/complex requests.

## 🛠️ Built With

- [Groq](https://groq.com/) - Ultra-fast LLM inference
- [Qwen 3 32B](https://console.groq.com/docs/models) - Generation model
- [Llama 3.3 70B](https://console.groq.com/docs/models) - Judge model

## 📄 License

This project is for assessment purposes only.

## 👤 Author

SAIKAT DAS - AI Engineer Candidate
```

---

**You are 100% ready to submit.** Just copy the `README.md` above, take the 5-6 screenshots mentioned, and add them to your Google Doc/PDF. Good luck! 🚀
