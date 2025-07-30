import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("player_data.csv")

# Select only needed columns
df = df[['Name', 'Height (in)', 'Weight (lb)']]
print(df.head()) #Confirm data loaded

# Plot Height vs Weight scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Height (in)', y='Weight (lb)')
plt.title('Height vs. Weight')
plt.xlabel('Height (inches)')
plt.ylabel('Weight (pounds)')
plt.grid(True)
plt.tight_layout()
plt.savefig("player_chart.png") # Save the chart to a PNG file
plt.show()