import pandas as pd

# Load the dataset
df = pd.read_csv('final_data_cut_10_days.csv')

# Display initial info to confirm structure
print("Original Data Head:")
print(df.head())
print(df.columns)

# Assume the first column is 'load' based on previous context
load_col_name = df.columns[0]

# Create the lag feature
# shift(1) moves data down by 1, so the current row gets the previous row's value
df['load(t-1)'] = df[load_col_name].shift(1)

# Reorder columns to place 'load(t-1)' as the first feature (index 1)
# Current columns: [Load, Feat1, Feat2, ..., load(t-1)]
# We want: [Load, load(t-1), Feat1, Feat2, ...]
cols = list(df.columns)
# Move the last column (newly created) to index 1
cols.insert(1, cols.pop(cols.index('load(t-1)')))
df = df[cols]

# Drop the first row which now contains NaN in the lag column
df_dropped = df.dropna()

# Save the new file
output_filename = 'final_data_with_lag.csv'
df_dropped.to_csv(output_filename, index=False)

print("\nNew Data Head:")
print(df_dropped.head())
print(f"\nSaved to {output_filename}")