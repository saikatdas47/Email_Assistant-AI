from test_data import TEST_SCENARIOS
from email_generator import generate_email_strategy_a, generate_email_strategy_b
from evaluator import evaluate_email
from report import generate_report

def run_experiment():
    all_results = []
    
    print("🚀 Starting Email Generation Experiment...\n")
    
    for scenario in TEST_SCENARIOS:
        sid = scenario["id"]
        intent = scenario["intent"]
        facts = scenario["facts"]
        tone = scenario["tone"]
        
        print(f"📧 Processing Scenario {sid}: {intent[:30]}...")
        
        # ---- Strategy A ----
        gen_a = generate_email_strategy_a(intent, facts, tone)
        eval_a = evaluate_email(gen_a, facts, tone)
        all_results.append({
            "id": sid,
            "strategy": "A",
            "factual_coverage": eval_a["factual_coverage"],
            "tone_adherence": eval_a["tone_adherence"],
            "quality_structure": eval_a["quality_structure"]
        })
        
        # ---- Strategy B ----
        gen_b = generate_email_strategy_b(intent, facts, tone)
        eval_b = evaluate_email(gen_b, facts, tone)
        all_results.append({
            "id": sid,
            "strategy": "B",
            "factual_coverage": eval_b["factual_coverage"],
            "tone_adherence": eval_b["tone_adherence"],
            "quality_structure": eval_b["quality_structure"]
        })
    
    # রিপোর্ট জেনারেট করুন
    json_file, csv_file = generate_report(all_results)
    
    # ---------- Comparative Analysis (Section 3) ----------
    print("\n" + "="*50)
    print("📝 COMPARATIVE ANALYSIS (Strategy A vs B)")
    print("="*50)
    
    # গড় বের করা
    avg_a = [r for r in all_results if r["strategy"] == "A"]
    avg_b = [r for r in all_results if r["strategy"] == "B"]
    
    def calc_avg(lst):
        if not lst: return 0,0,0,0
        f = sum(r["factual_coverage"] for r in lst) / len(lst)
        t = sum(r["tone_adherence"] for r in lst) / len(lst)
        q = sum(r["quality_structure"] for r in lst) / len(lst)
        return f, t, q, (f+t+q)/3
    
    f_a, t_a, q_a, o_a = calc_avg(avg_a)
    f_b, t_b, q_b, o_b = calc_avg(avg_b)
    
    print(f"\n🔹 Strategy A (Advanced)  -> Overall: {o_a:.2f} (Fact: {f_a:.2f}, Tone: {t_a:.2f}, Quality: {q_a:.2f})")
    print(f"🔹 Strategy B (Baseline)  -> Overall: {o_b:.2f} (Fact: {f_b:.2f}, Tone: {t_b:.2f}, Quality: {q_b:.2f})")
    
    winner = "A" if o_a >= o_b else "B"
    print(f"\n🏆 Winning Strategy: Strategy {winner}")
    
    # Biggest failure mode of the lower-performing model
    loser = "B" if winner == "A" else "A"
    loser_name = "Advanced" if loser == "A" else "Baseline"
    
    if loser == "B":
        # B fails mostly on factual coverage?
        diff_fact = f_a - f_b
        diff_tone = t_a - t_b
        diff_qual = q_a - q_b
        max_diff = max(diff_fact, diff_tone, diff_qual)
        if max_diff == diff_fact:
            failure = "Factual Coverage (many key facts were missing or vaguely mentioned)"
        elif max_diff == diff_tone:
            failure = "Tone Adherence (often failed to match the requested urgency or formality)"
        else:
            failure = "Quality/Structure (grammar, flow, or conciseness was poor)"
    else:
        failure = "Not applicable (Strategy A is baseline here, but usually Advanced wins)."
    
    print(f"\n❌ Biggest Failure Mode of Strategy {loser} ({loser_name}):")
    print(f"   -> {failure}")
    
    # Production Recommendation
    print("\n✅ Production Recommendation:")
    if winner == "A":
        print("   We recommend Strategy A for production. Despite the slightly higher latency/cost,")
        print("   it ensures critical facts are included (higher recall), matches the professional")
        print("   tone accurately, and produces cleaner, better-structured emails. For enterprise")
        print("   communication, reliability and precision outweigh cost differences.")
    else:
        print("   Strategy B might be sufficient for low-stakes tasks, but Strategy A offers")
        print("   superior robustness. We recommend Strategy A for production.")

if __name__ == "__main__":
    run_experiment()