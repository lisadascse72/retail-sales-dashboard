# Step 1: Import necessary libraries
import pandas as pd

# Step 2: Load the dataset
file_path = "retail_store_inventory.csv"  # Make sure the file is in the same folder
df = pd.read_csv(file_path)

# Step 3: Preview the data
print("First 5 rows of the dataset:")
print(df.head())
print("\nColumn names:")
print(df.columns)

# Step 4: Clean and transform data

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d')

# Create new columns for Month and Year
df['Month'] = df['Date'].dt.month
df['Year'] = df['Date'].dt.year
df['Month_Year'] = df['Date'].dt.to_period('M')  # For grouping later

# Calculate Revenue = Units Sold × Price
df['Revenue'] = df['Units Sold'] * df['Price']

# Calculate Discounted Price = Price - (Discount% of Price)
df['Discounted Price'] = df['Price'] * (1 - df['Discount'] / 100)

# Calculate Net Revenue = Units Sold × Discounted Price
df['Net Revenue'] = df['Units Sold'] * df['Discounted Price']

# Step 5: Check for null values
print("\nNull values in each column:")
print(df.isnull().sum())

# Step 6: Preview the new columns
print("\nPreview of new columns:")
print(df[['Date', 'Month_Year', 'Units Sold', 'Price', 'Discount', 'Revenue', 'Discounted Price', 'Net Revenue']].head())

# Step 7: Export the cleaned data
output_file = "cleaned_retail_data.csv"
df.to_csv(output_file, index=False)
print(f"\n✅ Cleaned data exported successfully to: {output_file}")
