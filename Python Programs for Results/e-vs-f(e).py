import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/sharodroy/Downloads/Results/Al/μ+/combined_output.csv'
data = pd.read_csv(file_path)

## Al, Au, Fe, Plastic, U
## e−, p, μ+, μ−

data.columns = data.columns.str.strip()

# Plotting the variation of f(E) as a histogram
plt.figure(figsize=(10, 6))
plt.hist(data['Energy'], bins=50, edgecolor='black')
plt.title('Variation of f(E) as a Function of Energy')
plt.xlabel('Energy')
plt.ylabel('Frequency (f(E))')
plt.grid(True)

plt.savefig('/home/sharodroy/Downloads/Results/Al/μ+/Energy_vs_f(E).png')

plt.show()