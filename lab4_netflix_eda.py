# Step 1: Import libraries
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv('netflix_titles.csv')

# Step 3: Display the first few rows of the dataset
print(df.head())

# Check the shape of the dataset
print("Dataset shape:", df.shape)

# Get an overview of the data types and null counts
print("\nDatat Info:")
print(df.info())

# Count missing values in each column
print("\mMissing values:")
print(df.isnull().sum())

# Drop rows where 'title' or 'type' is missing - they are essential
df = df.dropna(subset=['title', 'type'])
df['country'] = df['country'].fillna('Unknown')



