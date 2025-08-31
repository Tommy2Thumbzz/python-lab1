import os
print("USING DB:", os.path.abspath("bootcamp.db"))
import sqlite3
import matplotlib.pyplot as plt

# Connect to your bootcamp database
conn = sqlite3.connect("bootcamp.db")  # use relative path if .py file is in same folder
cur = conn.cursor()

# SQL query: average completion % per week
cur.execute("""
SELECT w.week_id, w.theme, ROUND(AVG(p.completion_percentage), 1) AS avg_progress_percent
FROM weeks w
LEFT JOIN milestones m ON m.week_id = w.week_id
LEFT JOIN progress p ON p.milestone_id = m.milestone_id
GROUP BY w.week_id, w.theme
ORDER BY w.week_id;
""")

rows = cur.fetchall()
print("DEBUG rows:", rows)
print("DEBUG count:", len(rows))

conn.close()

# Separate data for plotting
weeks = [row[0] for row in rows]
themes = [row[1] for row in rows]
progress = [row[2] if row[2] is not None else 0 for row in rows]
import matplotlib.ticker as mtick  # at top of file is fine too

# --- Clean, controlled plotting block (replace your old one) ---
fig, ax = plt.subplots()                 # fresh Figure/Axes so spacing is predictable
fig.subplots_adjust(top=0.80)            # reserve top space for subtitle

# Bars
colors = []
for val in progress:
    if val == 100:
        colors.append("green")  # completed
    elif val >=50:
        colors.append("orange")  # halfway
    else:
        colors.append("red")  # needs work

bars = ax.bar(weeks, progress, tick_label=themes, color=colors) 
import matplotlib.patches as mpatches  # put this at the top of your file if not already there

# Styled legend
# Create the legend patches (colored boxes)
legend_patches = [
    mpatches.Patch(color="green", label="Complete (100%)"),
    mpatches.Patch(color="orange", label="In Progress (50%+)"),
    mpatches.Patch(color="red", label="Needs Work (<50%)")
]
ax.legend(
    handles=legend_patches,
    loc="upper right",
    fontsize=8,
    frameon=True,
    framealpha=0.8,       # slightly transparent background
    facecolor="white",    # clean white background
    edgecolor="lightgray" # subtle border
)

ax.legend(handles=legend_patches, loc="upper right")


# Reserve more space above the plot
fig.subplots_adjust(top=0.75)

# Main title and subtitle using figure-level text (more control)
fig.text(
    0.5, 0.98, "Average Progress % per Week",
    ha="center", va="top", fontsize=12, fontweight="bold"
)

fig.text(
    0.5, 0.94, "Tracking weekly bootcamp progress from SQL → Python → Visualization",
    ha="center", va="top", fontsize=9, color="gray"
)

fig.subplots_adjust(top=0.88)





# Y-axis as %
ax.set_ylim(0, 100)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(100))

# % labels above each bar
for bar, value in zip(bars, progress):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h + 2, f"{value:.0f}%", ha="center", va="bottom", fontsize=10)

# Axis labels
ax.set_xlabel("Week / Theme")
ax.set_ylabel("Avg Progress %")

# Save + show
fig.savefig("progress_report.png", dpi=150, bbox_inches="tight")
fig.savefig("progress_report.pdf", dpi=150, bbox_inches="tight")
plt.show()

