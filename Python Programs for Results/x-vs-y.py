import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/sharodroy/Downloads/Results/U/μ−/100000MeV/output.csv'

# /Al/e−/
# /Al/p/
# /Al/μ+/
# /Al/μ−/

# /Au/e−/
# /Au/p/
# /Au/μ+/
# /Au/μ−/

# /Fe/e−/
# /Fe/p/
# /Fe/μ+/
# /Fe/μ−/

# /Plastic/e−/
# /Plastic/p/
# /Plastic/μ+/
# /Plastic/μ−/

# /U/e−/
# /U/p/
# /U/μ+/
# /U/μ−/

data = pd.read_csv(file_path)

data.columns = data.columns.str.strip()

x = data['PositionX']
y = data['PositionY']

# Create the plot
plt.figure(figsize=(10, 6))
plt.scatter(x, y, color='blue', marker='o')
plt.title('PositionX vs PositionY')
plt.xlabel('PositionX')
plt.ylabel('PositionY')
plt.grid(True)

plt.savefig('/home/sharodroy/Downloads/Results/U/μ−/100000MeV/PositionX_vs_PositionY.png')

plt.show()