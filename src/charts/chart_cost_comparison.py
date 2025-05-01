import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from math import pi

# 6 Updated Cost Metrics with line breaks for readability
cost_metrics = [
    'Labor Cost\n(Human Gathered)',
    'Labor Cost\n(Human Processed)',
    'Labor Cost\n(Human Reinforced)',
    'Auto. Cost\n(Real-Time Gathered)',
    'Auto. Cost\n(Real-Time Processed)',
    'Auto. Cost\n(Real-Time Reinforced)'
]

mini_llm_traditional_costs = [0.40, 0.30, 0.50, 0.05, 0.05, 0.40]
mini_llm_interactive_costs = [0.10, 0.08, 0.20, 0.02, 0.02, 0.15]
chatgpt_traditional_costs = [0.80, 0.60, 0.90, 0.20, 0.40, 1.00]
chatgpt_interactive_costs = [0.20, 0.15, 0.30, 0.05, 0.05, 0.80]

# Radar chart function
def create_radar_chart(ax, metrics, traditional_data, interactive_data, title, ylim_max):
    N = len(metrics)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.spines['polar'].set_visible(False)
    ax.grid(color='grey', linestyle='dotted', linewidth=1.25)

    # Extend data for circular completion
    traditional_data += traditional_data[:1]
    interactive_data += interactive_data[:1]

    # Plot lines
    ax.plot(angles, traditional_data, linewidth=2, linestyle='solid', label='Traditional', color='blue')
    ax.fill(angles, traditional_data, 'blue', alpha=0.1)

    ax.plot(angles, interactive_data, linewidth=2, linestyle='solid', label='Interactive', color='orange')
    ax.fill(angles, interactive_data, 'orange', alpha=0.1)

    # Axes setup
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics, fontsize=9)
    for label in ax.get_xticklabels():
        label.set_fontweight('bold')
        label.set_color('black')

    ax.set_ylim(0, ylim_max)
    ax.set_title(title, size=12, y=1.08)

    # Legend styling
    legend = ax.legend(loc='lower left', fontsize=9, frameon=True)
    legend.get_frame().set_edgecolor('grey')
    legend.get_frame().set_linewidth(1.0)
    legend.get_frame().set_facecolor('whitesmoke')
    legend.get_frame().set_boxstyle('round,pad=0.3')

# Create figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8), subplot_kw=dict(polar=True),
                               gridspec_kw={'wspace': 0.3})

# Generate radar charts
create_radar_chart(ax1, cost_metrics, mini_llm_traditional_costs.copy(), mini_llm_interactive_costs.copy(),
                   '- Mini LLM -', ylim_max=0.6)

create_radar_chart(ax2, cost_metrics, chatgpt_traditional_costs.copy(), chatgpt_interactive_costs.copy(),
                   '- ChatGPT -', ylim_max=1.2)

# Resize and recenter plots
# Adjust radars individually to balance left/right spacing
# Shrink and shift left for ax1, shift right for ax2
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


# Top Title Line 1
fig.text(
    0.5, 0.965,
    '- Traditional Dialogues Mode versus Interactive Dialogues Mode -',
    ha='center', va='top', fontsize=14
)

# Top Title Line 2
fig.text(
    0.5, 0.935,
    'Performance Scores of Cost Metrics - Gathered and Processed 1M Human-Quality Explanations',
    ha='center', va='top', fontsize=12, style='italic', weight='bold'
)

# Top Subtitle Line 3
fig.text(
    0.5, 0.865,
    'Note: The lower scores are the better.',
    ha='center', va='top', fontsize=11, style='italic'
)

# Horizontal line to separate title block
line = Line2D([0.0, 1.0], [0.89, 0.89], transform=fig.transFigure, color='lightgrey', linewidth=0.5)
fig.add_artist(line)

# Layout adjustments
plt.subplots_adjust(top=0.85, bottom=0, left=0.07, right=0.93, wspace=0.25)

# Save and show
plt.savefig('radar_chart_costs_metrics.png', bbox_inches='tight')
plt.show()
