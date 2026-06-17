import json
import csv
from datetime import datetime

def generate_report(results: list, filename_prefix="evaluation_report"):
    """
    results: একটি লিস্ট, প্রতিটি ডিক্টে থাকবে:
    {
      "id": 1,
      "strategy": "A",
      "factual_coverage": 8.5,
      "tone_adherence": 9.0,
      "quality_structure": 9.5
    }
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # JSON Output
    json_file = f"{filename_prefix}_{timestamp}.json"
    with open(json_file, "w") as f:
        json.dump(results, f, indent=2)
    print(f"✅ JSON report saved: {json_file}")
    
    # CSV আউটপুট
    csv_file = f"{filename_prefix}_{timestamp}.csv"
    fieldnames = ["id", "strategy", "factual_coverage", "tone_adherence", "quality_structure"]
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow({
                "id": row["id"],
                "strategy": row["strategy"],
                "factual_coverage": row["factual_coverage"],
                "tone_adherence": row["tone_adherence"],
                "quality_structure": row["quality_structure"]
            })
    print(f"✅ CSV report saved: {csv_file}")
    
    # Print overall averages for each strategy
    print("\n" + "="*50)
    print("📊 OVERALL AVERAGE SCORES")
    print("="*50)
    for strategy in ["A", "B"]:
        strat_results = [r for r in results if r["strategy"] == strategy]
        if strat_results:
            avg_fact = sum(r["factual_coverage"] for r in strat_results) / len(strat_results)
            avg_tone = sum(r["tone_adherence"] for r in strat_results) / len(strat_results)
            avg_qual = sum(r["quality_structure"] for r in strat_results) / len(strat_results)
            overall = (avg_fact + avg_tone + avg_qual) / 3
            print(f"\n🔹 Strategy {strategy} (Avg over {len(strat_results)} scenarios):")
            print(f"   Factual Coverage : {avg_fact:.2f}")
            print(f"   Tone Adherence   : {avg_tone:.2f}")
            print(f"   Quality/Structure: {avg_qual:.2f}")
            print(f"   🏆 Overall       : {overall:.2f}")

    return json_file, csv_file