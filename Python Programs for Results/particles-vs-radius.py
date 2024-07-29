import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/sharodroy/Downloads/Results/U/μ−/100000MeV/output.csv'

## Al, Au, Fe, Plastic, U
## e−, p, μ+, μ−
## 100MeV, 10000MeV, 100000MeV

data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

# Create a histogram to plot the number of particles vs. radius
plt.figure(figsize=(10, 6))
plt.hist(data['Radius'], bins=50, edgecolor='black')
plt.title('Number of Particles vs Radius')
plt.xlabel('Radius')
plt.ylabel('Number of Particles')
plt.grid(True)

plt.savefig('/home/sharodroy/Downloads/Results/U/μ−/100000MeV/particles_vs_radius.png')

plt.show()