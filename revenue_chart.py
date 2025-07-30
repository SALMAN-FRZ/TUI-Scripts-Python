import matplotlib.pyplot as plt
import numpy as np

# Data from the chart
labels = ['March', 'April', 'May', 'June', 'July', 'August (Proj.)']
data = [0.8, 1.0, 1.2, 1.5, 2.1, 3.0]
x_pos = np.arange(len(labels))

# Colors from the energeticPlayfulPalette
primary_color = '#4F46E5'
primary_color_rgba = (79/255, 70/255, 229/255, 0.1) # Converted for fill_between
text_color = '#1E293B'
neutral_color = '#6B7280'
grid_color = '#E2E8F0'

# Create the plot
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(10, 6))

# Plot the line with tension effect (using a spline for a smooth curve)
from scipy.interpolate import make_interp_spline
x_new = np.linspace(x_pos.min(), x_pos.max(), 300)
spl = make_interp_spline(x_pos, data, k=3)  # k=3 for cubic spline
data_smooth = spl(x_new)

ax.plot(x_new, data_smooth, color=primary_color, linewidth=2)

# Add the fill color underneath the line
ax.fill_between(x_new, data_smooth, color=primary_color_rgba)

# Add the original data points
ax.plot(x_pos, data, 'o', color=primary_color, markersize=8, markerfacecolor=primary_color, markeredgecolor='white')


# Set titles and labels
ax.set_title("Monthly Sales Revenue Growth", fontsize=18, weight='bold', color=text_color, pad=20)
ax.set_ylabel("Revenue in INR Lakhs", fontsize=12, color=neutral_color)
ax.set_xticks(x_pos)
ax.set_xticklabels(labels, fontsize=12, color=neutral_color)

# Customize grid and spines
ax.grid(color=grid_color)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color(grid_color)
ax.spines['bottom'].set_color(grid_color)

# Set y-axis to start at zero
ax.set_ylim(0)

# Add data labels on top of the points
for i, val in enumerate(data):
    ax.text(i, val + 0.1, f'{val:.1f}L', ha='center', va='bottom', fontsize=10, color=primary_color, weight='bold')


plt.tight_layout()
plt.savefig('revenue_growth_chart.png')
plt.show()