import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Explanation scales
mini_scales = np.array([1_000, 5_000, 10_000, 50_000, 100_000])
chatgpt_scales = np.array([10_000, 50_000, 100_000, 500_000, 1_000_000])

# Cost submetrics (Mini LLM)
mini_llm_cost_curves = np.array([
    np.interp(mini_scales, [1_000, 100_000], [0.40, 0.25]),  # Human-Gathered
    np.interp(mini_scales, [1_000, 100_000], [0.30, 0.10]),  # Human-Processed
    np.interp(mini_scales, [1_000, 100_000], [0.50, 0.30]),  # Human-Reinforced
    np.interp(mini_scales, [1_000, 100_000], [0.05, 0.02]),  # Auto-Gathered
    np.interp(mini_scales, [1_000, 100_000], [0.05, 0.02]),  # Auto-Processed
    np.interp(mini_scales, [1_000, 100_000], [0.40, 0.15]),  # Auto-Reinforced
])

# Cost submetrics (ChatGPT)
chatgpt_cost_curves = np.array([
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.80, 0.60]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.60, 0.20]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.90, 0.70]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.20, 0.05]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.40, 0.05]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [1.00, 0.80]),
])

cost_labels = [
    'Human-Gathered', 'Human-Processed', 'Human-Reinforced',
    'Auto-Gathered', 'Auto-Processed', 'Auto-Reinforced'
]
cost_colors = cm.get_cmap('tab10', len(cost_labels))

# Quality submetrics (Mini LLM)
mini_llm_quality_curves = np.array([
    np.interp(mini_scales, [1_000, 100_000], [0.32, 0.70]),  # Novelty
    np.interp(mini_scales, [1_000, 100_000], [0.54, 0.68]),  # Specificity
    np.interp(mini_scales, [1_000, 100_000], [0.41, 0.68]),  # Tone
])

# Quality submetrics (ChatGPT)
chatgpt_quality_curves = np.array([
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.45, 0.79]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.77, 0.81]),
    np.interp(chatgpt_scales, [10_000, 1_000_000], [0.72, 0.83]),
])

quality_labels = [
    'Novelty and Erudition',
    'Specificity and Precision',
    'Human-Tone Mimicked'
]
quality_colors = cm.get_cmap('Set2', len(quality_labels))

# Plot
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Cost subplot
for i, label in enumerate(cost_labels):
    ax[0].plot(mini_scales, mini_llm_cost_curves[i], linestyle='-', marker='o',
               color=cost_colors(i), label=f'Mini LLM – {label}')
    ax[0].plot(chatgpt_scales, chatgpt_cost_curves[i], linestyle='--', marker='s',
               color=cost_colors(i), label=f'ChatGPT – {label}')

ax[0].set_xscale('log')
ax[0].invert_yaxis()
ax[0].set_title('Cost Saving Curve (Lower is Better)')
ax[0].set_xlabel('Number of Explanations (log scale)')
ax[0].set_ylabel('Relative Cost Score')
ax[0].grid(True, linestyle='dotted', alpha=0.6)
ax[0].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5))

# Quality subplot
for i, label in enumerate(quality_labels):
    ax[1].plot(mini_scales, mini_llm_quality_curves[i], linestyle='-', marker='o',
               color=quality_colors(i), label=f'Mini LLM – {label}')
    ax[1].plot(chatgpt_scales, chatgpt_quality_curves[i], linestyle='--', marker='s',
               color=quality_colors(i), label=f'ChatGPT – {label}')

ax[1].set_xscale('log')
ax[1].set_title('Quality Improvement Curve (Higher is Better)')
ax[1].set_xlabel('Number of Explanations (log scale)')
ax[1].set_ylabel('Relative Quality Score')
ax[1].grid(True, linestyle='dotted', alpha=0.6)
ax[1].legend(fontsize=8, loc='center left', bbox_to_anchor=(1, 0.5))

plt.tight_layout()
plt.show()
