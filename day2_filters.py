import pandas as pd

# Load and clean data
df = pd.read_csv("nba_player_stats.csv.csv")
df.columns = df.columns.str.strip().str.replace('"', '').str.replace("'", '')

# Players taller than 72 inches (6 feet)
tall_players = df[df["Height(Inches)"] > 72]
print("\nPlayers taller than 6 feet (72 inches):")
print(tall_players)

# Sort players by weight (heaviest to lightest)
sorted_by_weight = df.sort_values(by="Weight(Pounds)", ascending=False)
print("\nPlayers sorted by weight (heaviest to lightest):")
print(sorted_by_weight.head(10)) # show top 10 heaviest

# Calculate average height
average_height = df["Height(Inches)"].mean()
print(f"\nAverage height: {average_height:.2f} inches")

# Players shorter than average
short_players = df[df["Height(Inches)"] < average_height]
print("\nPlayers shorter than average:")
print(short_players.head(10)) # show top 10

# Export short players sorted by height (ascending)
short_players_sorted = short_players.sort_values(by="Height(Inches)")
short_players_sorted.to_csv("short_players.csv", index=False)
print("\nSorted filtered data saved to short_players.csv")
