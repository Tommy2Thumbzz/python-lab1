import pandas as pd

# Step 1: Load the CSV
df = pd.read_csv("nba_player_stats.csv.csv")

# Step 2: Clean column names
df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", '')

# Step 3: Preview the data
print("\nPreview of the dataset:")
print(df.head())
print("\nColumn names:")
print(df.columns)

# Step 4: Calculate stats
avg_height = df["Height(Inches)"].mean()
avg_weight = df["Weight(Pounds)"].mean()
max_height = df["Height(Inches)"].max()
min_height = df["Height(Inches)"].min()
max_weight = df["Weight(Pounds)"].max()
min_weight = df["Weight(Pounds)"].min()

# Step 5: Print stats
print("\n=== Player Stats Summary ===")
print(f"Average Height: {avg_height:.2f} inches")
print(f"Average Weight: {avg_weight:.2f} pounds")
print(f"Tallest Player: {max_height} inches")
print(f"Shortest Player: {min_height} inches")
print(f"Heaviest Player: {max_weight} pounds")
print(f"Lightest Player: {min_weight} pounds")

import matplotlib.pyplot as plt

# Step 6 Plot a bar chart of the first 10 players' weights
players = df.head(10) # first 10 rows
names = [f"Player {i+1}" for i in players.index]
weights = players["Weight(Pounds)"]

plt.figure(figsize=(10, 6))
plt.bar(names, weights, color= 'mediumslateblue')
plt.xlabel("Players")
plt.ylabel("Weight (Pounds)")
plt.title("Weight of First 10 Players")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("player_weights_chart.png")

# Show the chart
plt.show()