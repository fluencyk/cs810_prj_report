import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from math import pi

# Quality metrics (3 axes)
quality_metrics = [
    'Novelty and Erudition',
    'Specificity and Precision',
    'Human-Tone Mimicked'
]

mini_llm_traditional_qualities = [0.32, 0.54, 0.41]
mini_llm_interactive_qualities = [0.70, 0.68, 0.68]
chatgpt_traditional_qualities = [0.45, 0.77, 0.72]
chatgpt_interactive_qualities = [0.79, 0.81, 0.83]

# Reusable radar chart function
def create_radar_chart(ax, metrics, traditional_data, interactive_data, title, ylim_max):
    N = len(metrics)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    traditional_data += traditional_data[:1]
    interactive_data += interactive_data[:1]

    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.spines['polar'].set_visible(False)
    ax.grid(color='grey', linestyle='dotted', linewidth=1.25)

    ax.plot(angles, traditional_data, linewidth=2, linestyle='solid', label='Traditional', color='green')
    ax.fill(angles, traditional_data, 'blue', alpha=0.1)

    ax.plot(angles, interactive_data, linewidth=2, linestyle='solid', label='Interactive', color='magenta')
    ax.fill(angles, interactive_data, 'orange', alpha=0.1)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, fontsize=8)  # smaller text
    for label in ax.get_xticklabels():
        label.set_fontweight('bold')
        label.set_color('black')

    ax.set_ylim(0, ylim_max)
    ax.set_title(title, size=12, y=1.12)

    legend = ax.legend(loc='lower left', fontsize=9, frameon=True)
    legend.get_frame().set_edgecolor('grey')
    legend.get_frame().set_linewidth(1.0)
    legend.get_frame().set_facecolor('whitesmoke')
    legend.get_frame().set_boxstyle('round,pad=0.3')

# Create radar figure
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), subplot_kw=dict(polar=True), gridspec_kw={'wspace': 0.3})

# Plot qualities
create_radar_chart(ax1, quality_metrics,
                   mini_llm_traditional_qualities.copy(),
                   mini_llm_interactive_qualities.copy(),
                   '- Mini LLM -', ylim_max=0.9)

create_radar_chart(ax2, quality_metrics,
                   chatgpt_traditional_qualities.copy(),
                   chatgpt_interactive_qualities.copy(),
                   '- ChatGPT -', ylim_max=0.9)

# Adjust positions
ax1_box = ax1.get_position()
ax1.set_position([
    ax1_box.x0 - 0.01, ax1_box.y0 + 0.06,
    ax1_box.width * 0.75, ax1_box.height * 0.7
])
ax2_box = ax2.get_position()
ax2.set_position([
    ax2_box.x0 + 0.01, ax2_box.y0 + 0.06,
    ax2_box.width * 0.75, ax2_box.height * 0.7
])

# Top Titles
fig.text(0.5, 0.965,
         '- Traditional Dialogues Mode versus Interactive Dialogues Mode -',
         ha='center', va='top', fontsize=14)

fig.text(0.5, 0.935,
         'Performance Scores of Quality Metrics - Learned 1M Human-Quality Explanations From Both Different Modes',
         ha='center', va='top', fontsize=12, style='italic', weight='bold')

fig.text(0.5, 0.865,
         'Note: The higher scores are the better.',
         ha='center', va='top', fontsize=11, style='italic')

# Horizontal split line
fig.add_artist(Line2D([0.0, 1.0], [0.89, 0.89], transform=fig.transFigure, color='lightgrey', linewidth=0.5))

# Final layout
plt.subplots_adjust(top=0.85, bottom=0, left=0.07, right=0.93, wspace=0.25)

# Save or show
plt.savefig('radar_chart_quality_metrics.png', bbox_inches='tight')
plt.show()
