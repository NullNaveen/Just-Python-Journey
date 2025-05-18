#image generation code in chat gpt
'''
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define the hierarchy levels and positions
levels = [
    {"level": "Producers", "examples": "Plants", "position": (0.5, 0.9)},
    {"level": "Primary Consumers", "examples": "Herbivores (e.g., rabbits, insects)", "position": (0.5, 0.7)},
    {"level": "Secondary Consumers", "examples": "Small Carnivores (e.g., snakes, birds)", "position": (0.5, 0.5)},
    {"level": "Tertiary Consumers", "examples": "Top Carnivores (e.g., hawks, foxes)", "position": (0.5, 0.3)},
    {"level": "Decomposers", "examples": "Fungi and Bacteria", "position": (0.5, 0.1)}
]

# Add rectangles and text for each level
for level in levels:
    ax.add_patch(patches.Rectangle((level["position"][0] - 0.25, level["position"][1] - 0.05), 0.5, 0.1, 
                                   edgecolor='black', facecolor='lightblue'))
    ax.text(level["position"][0], level["position"][1], f"{level['level']}\n{level['examples']}", 
            horizontalalignment='center', verticalalignment='center', fontsize=12)

# Draw arrows between levels
for i in range(len(levels) - 1):
    ax.annotate('', xy=levels[i+1]["position"], xytext=levels[i]["position"],
                arrowprops=dict(facecolor='black', shrink=0.05))

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save the figure
file_path = "/mnt/data/food_chain_hierarchy.png"
plt.savefig(file_path, bbox_inches='tight')

file_path
'''

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Define the hierarchy levels and positions
levels = [
    {"level": "Producers", "examples": "Plants", "position": (0.5, 0.9)},
    {"level": "Primary Consumers", "examples": "Herbivores (e.g., rabbits, insects)", "position": (0.5, 0.7)},
    {"level": "Secondary Consumers", "examples": "Small Carnivores (e.g., snakes, birds)", "position": (0.5, 0.5)},
    {"level": "Tertiary Consumers", "examples": "Top Carnivores (e.g., hawks, foxes)", "position": (0.5, 0.3)},
    {"level": "Decomposers", "examples": "Fungi and Bacteria", "position": (0.5, 0.1)}
]

# Add rectangles and text for each level
for level in levels:
    ax.add_patch(patches.Rectangle((level["position"][0] - 0.25, level["position"][1] - 0.05), 0.5, 0.1, 
                                   edgecolor='black', facecolor='lightblue'))
    ax.text(level["position"][0], level["position"][1], f"{level['level']}\n{level['examples']}", 
            horizontalalignment='center', verticalalignment='center', fontsize=12)

# Draw arrows between levels
for i in range(len(levels) - 1):
    ax.annotate('', xy=levels[i+1]["position"], xytext=levels[i]["position"],
                arrowprops=dict(facecolor='black', shrink=0.05))

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Define the new file path to save the figure
home_dir = os.path.expanduser('~')
file_path = os.path.join(home_dir, 'Documents', 'food_chain_hierarchy.png')

# Save the figure
plt.savefig(file_path, bbox_inches='tight')

print(f"File saved at {file_path}")
