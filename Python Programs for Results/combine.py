import pandas as pd

# Define the paths to the CSV files
file_paths = [
    '/home/sharodroy/Downloads/Results/U/μ+/100MeV/output.csv',
    '/home/sharodroy/Downloads/Results/U/μ+/10000MeV/output.csv',
    '/home/sharodroy/Downloads/Results/U/μ+/100000MeV/output.csv'
]

## Al, Au, Fe, Plastic, U
## e−, p, μ+, μ−

# Read the CSV files into DataFrames
dfs = [pd.read_csv(file_path) for file_path in file_paths]

# Combine the DataFrames into a single DataFrame
combined_df = pd.concat(dfs)

# Define the path to save the combined CSV file
output_path = '/home/sharodroy/Downloads/Results/U/μ+/combined_output.csv'

# Save the combined DataFrame to a CSV file
combined_df.to_csv(output_path, index=False)

print(f'Combined CSV file saved to {output_path}')
