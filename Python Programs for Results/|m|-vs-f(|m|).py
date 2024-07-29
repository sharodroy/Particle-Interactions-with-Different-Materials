import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/sharodroy/Downloads/Results/U/μ+/100MeV/output.csv'

## Al, Au, Fe, Plastic, U
## e−, p, μ+, μ−
## 100MeV, 10000MeV, 100000MeV

data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

# Plotting the variation of f(|M|) as a histogram
plt.figure(figsize=(10, 6))
plt.hist(data['|Momentum|'], bins=50, edgecolor='black')
plt.title('Variation of f(|M|) as a Function of |Momentum|')
plt.xlabel('|Momentum|')
plt.ylabel('Frequency (f(|M|))')
plt.grid(True)

plt.savefig('/home/sharodroy/Downloads/Results/U/μ+/100MeV/|Momentum|_vs_f(|M|).png')

plt.show()