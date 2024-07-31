import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/sharodroy/Downloads/Results/U/p/100,000MeV/output.csv'

data = pd.read_csv(file_path)
data.columns = data.columns.str.strip()

# Plot 1: Number of Particles vs Radius
plt.figure(figsize=(10, 6))
plt.hist(data['Radius'], bins=50, edgecolor='black')
plt.title('Number of Particles vs Radius')
plt.xlabel('Radius')
plt.ylabel('Number of Particles')
plt.grid(True)
plt.savefig('/home/sharodroy/Downloads/Results/U/p/100,000MeV/particles_vs_radius.png')

# Plot 2: PositionX vs PositionY
x = data['PositionX']
y = data['PositionY']

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', marker='o')
plt.title('PositionX vs PositionY')
plt.xlabel('PositionX')
plt.ylabel('PositionY')
plt.grid(True)
plt.savefig('/home/sharodroy/Downloads/Results/U/p/100,000MeV/PositionX_vs_PositionY.png')

# Plot 3: Variation of f(|M|) as a Function of |Momentum|
plt.figure(figsize=(10, 6))
plt.hist(data['|Momentum|'], bins=50, edgecolor='black')
plt.title('Variation of f(|M|) as a Function of |Momentum|')
plt.xlabel('|Momentum|')
plt.ylabel('Frequency (f(|M|))')
plt.grid(True)
plt.savefig('/home/sharodroy/Downloads/Results/U/p/100,000MeV/|Momentum|_vs_f(|M|).png')
