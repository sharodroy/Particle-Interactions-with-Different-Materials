import pandas as pd

file_paths = [
    '/home/sharodroy/Downloads/Results/U/μ+/100MeV/output.csv',
    '/home/sharodroy/Downloads/Results/U/μ+/10000MeV/output.csv',
    '/home/sharodroy/Downloads/Results/U/μ+/100000MeV/output.csv'
]

## Al, Au, Fe, Plastic, U
## e−, p, μ+, μ−

dfs = [pd.read_csv(file_path) for file_path in file_paths]

combined_df = pd.concat(dfs)

output_path = '/home/sharodroy/Downloads/Results/U/μ+/combined_output.csv'

combined_df.to_csv(output_path, index=False)

print(f'Combined CSV file saved to {output_path}')