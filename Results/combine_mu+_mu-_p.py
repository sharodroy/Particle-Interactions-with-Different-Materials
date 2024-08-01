import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

file_paths = [
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Al_mu+_1,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Al_mu+_10,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Al_mu+_100,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Au_mu+_1,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Au_mu+_10,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Au_mu+_100,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Fe_mu+_1,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Fe_mu+_10,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Fe_mu+_100,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Plastic_mu+_1,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Plastic_mu+_10,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Plastic_mu+_100,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/U_mu+_1,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/U_mu+_10,000MeV_PositionX_vs_PositionY.png",
    "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/U_mu+_100,000MeV_PositionX_vs_PositionY.png"
]

materials = ["Al", "Au", "Fe", "Plastic", "U"]
energies = ["1,000 MeV", "10,000 MeV", "100,000 MeV"]

fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(30, 30))
fig.suptitle('Positively Charged Muons - PositionX_vs_PositionY', fontsize=24)

# Plot each image in its respective subplot
for i, ax in enumerate(axes.flat):
    img = mpimg.imread(file_paths[i])
    ax.imshow(img)
    material = materials[i // 3]
    energy = energies[i % 3]
    ax.set_title(f"{material} at {energy}", fontsize=14)
    ax.axis('off')  # Turn off axis

plt.tight_layout(rect=[0, 0, 1, 0.96])

# Save the figure
output_path = "/home/sharodroy/Downloads/Data Analysis/PositionX_vs_PositionY/mu+/Combined.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.close(fig)
print(f"Combined image saved at {output_path}")
