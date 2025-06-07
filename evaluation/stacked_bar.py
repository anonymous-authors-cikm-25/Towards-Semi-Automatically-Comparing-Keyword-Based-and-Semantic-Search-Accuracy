import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


file1 = "rag_1_3.csv"
file2 = "confluence_1_3.csv"

def get_aggregated_results_from_files(filename):
    # Store results for both files
    df = pd.read_csv(filename, sep=";", header=None)
    # Try both integer and string lookup for robustness
    counts = df[1].value_counts()
    # Try integer first, then string (in case data is string)
    result = [
        counts.get(1, 0) or counts.get('1', 0),
        counts.get(2, 0) or counts.get('2', 0),
        counts.get(3, 0) or counts.get('3', 0)
    ]

    return result

data_file1 = get_aggregated_results_from_files(file1)
data_file2 = get_aggregated_results_from_files(file2)

colors = [
   '#1f6f6f',  
   '#54a1a1',
    '#9fc8c8'
]
# Plot data creation
categories = ['1', '2', '3']

# Creation of stacked bar diagram
fig, ax = plt.subplots(figsize=(8, 4))

ax.barh(file1, data_file1[0], color=colors[0])
ax.barh(file1, data_file1[1], left=data_file1[0], color=colors[1])
ax.barh(file1, data_file1[2], left=np.sum(data_file1[:2]), color=colors[2])

ax.barh(file2, data_file2[0], color=colors[0], label='1')
ax.barh(file2, data_file2[1], left=data_file2[0], color=colors[1], label='2')
ax.barh(file2, data_file2[2], left=np.sum(data_file2[:2]), color=colors[2], label='3')

x_offset = 0
for i, value in enumerate(data_file1):
    ax.text(x_offset + value / 2, 0, str(value), va='center', ha='center', fontsize=12, color='white', fontweight='bold')
    x_offset += value

# Add values on top of the bars (S2)
x_offset = 0
for i, value in enumerate(data_file2):
    ax.text(x_offset + value / 2, 1, str(value), va='center', ha='center', fontsize=12, color='white', fontweight='bold')
    x_offset += value

# Legend
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

ax.set_xlabel("Number of queries",fontsize=12)
ax.set_ylabel('')
plt.tight_layout()
#plt.savefig("conf_vs_rag_stacked_bar_800_400_with_nmrcal_values.pdf")
plt.show()
