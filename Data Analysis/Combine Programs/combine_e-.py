import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

file_paths = [
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Al_e-_1,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Al_e-_10,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Al_e-_100,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Au_e-_1,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Au_e-_10,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Au_e-_100,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Fe_e-_1,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Fe_e-_10,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Fe_e-_100,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Plastic_e-_1,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Plastic_e-_10,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Plastic_e-_100,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/U_e-_1,000MeV_|Momentum|_vs_f(|M|).png",
    "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/U_e-_10,000MeV_|Momentum|_vs_f(|M|).png",
    # The 100,000 MeV for Uranium is not included
]

materials = ["Al", "Au", "Fe", "Plastic", "U"]
energies = ["1,000 MeV", "10,000 MeV", "100,000 MeV"]

# Create the figure and axes for a 5x3 grid, excluding 100,000 MeV for Uranium
fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(30, 30))
fig.suptitle('Electrons - |Momentum|_vs_f(|M|)', fontsize=24)

for i, ax in enumerate(axes.flat):
    # Handle the missing 100,000 MeV for Uranium by skipping the last plot
    if i == len(file_paths):
        ax.axis('off')  # Leave the last subplot empty
        continue
    
    img = mpimg.imread(file_paths[i])
    ax.imshow(img)
    material = materials[i // 3]
    energy = energies[i % 3]
    ax.set_title(f"{material} at {energy}", fontsize=14)
    ax.axis('off')  # Turn off axis

plt.tight_layout(rect=[0, 0, 1, 0.96])

output_path = "/home/sharodroy/Downloads/Data Analysis/|Momentum|_vs_f(|M|)/e-/Combined.png"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
plt.savefig(output_path)
plt.close(fig)
print(f"Combined image saved at {output_path}")
