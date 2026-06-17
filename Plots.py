import matplotlib.pyplot as plt
import numpy as np

# === YOUR DATA (from the evaluation report) ===
metrics = ['Factual Coverage', 'Tone Adherence', 'Quality/Structure', 'Overall']
strategy_a = [9.40, 9.20, 9.00, 9.20]   # Strategy A (Advanced)
strategy_b = [9.50, 9.10, 9.20, 9.27]   # Strategy B (Baseline)

# === PLOT CONFIGURATION ===
x = np.arange(len(metrics))              # Label locations
width = 0.35                             # Width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Create the grouped bars
rects1 = ax.bar(x - width/2, strategy_a, width, label='Strategy A (Advanced)', color='#2E86C1', edgecolor='black')
rects2 = ax.bar(x + width/2, strategy_b, width, label='Strategy B (Baseline)', color='#E67E22', edgecolor='black')

# === LABELS & FORMATTING ===
ax.set_xlabel('Evaluation Metrics', fontsize=13, fontweight='bold')
ax.set_ylabel('Score (0 - 10)', fontsize=13, fontweight='bold')
ax.set_title('Comparative Performance: Strategy A vs Strategy B', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=10)
ax.legend(fontsize=12, loc='upper left')
ax.set_ylim(7, 10.5)  # Give a little headroom for labels
ax.grid(axis='y', linestyle='--', alpha=0.6)

# === ADD VALUE LABELS ON TOP OF BARS ===
def add_value_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height:.2f}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', fontsize=8, fontweight='bold')

add_value_labels(rects1)
add_value_labels(rects2)

# === SHOW / SAVE THE PLOT ===
plt.tight_layout()
plt.savefig('evaluation_comparison_plot.png', dpi=300)  # Saves as high-res image
plt.show()

print("✅ Plot saved as 'evaluation_comparison_plot.png'")