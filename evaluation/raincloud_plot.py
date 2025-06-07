import matplotlib.pyplot as plt
import pandas as pd
import ptitprince as pt

file1 = 'retrieval_rag_1_10.csv'
file2 = 'confluence_1_10.csv'
# Load the CSV data into a pandas DataFrame without treating the first row as column headers
df_file1 = pd.read_csv(file1, header=None, delimiter=";")
df_file2 = pd.read_csv(file2, header=None, delimiter=";")

values_file1 = df_file1[1]
values_file2 = df_file2[1]

# Combine data for boxplot
data_group2 = [values_file2, values_file1]
# Labels for the comparison
labels_group2 = [file2, file1]

# Create a figure and axis for the plot
plt.figure(figsize=(6, 4))

# Prepare data
values_file1_numpy = values_file1.to_numpy()
values_file2_numpy = values_file2.to_numpy()

# Create tidy dataframe
df = pd.DataFrame({
    "value": list(values_file2_numpy) + list(values_file1_numpy),
    "group": [file2] * len(values_file2_numpy) + [file1] * len(values_file1_numpy)
})

# Plot
f, ax = plt.subplots()  # Increase figure size for better label display
pt.RainCloud(x='group', y='value', data=df, bw=.2, width_viol=.6, ax=ax, orient='h')

ax.set_xlabel("Information retrieval accuracy (equivalence classes)", fontsize=12)
ax.set_ylabel("Search approach", fontsize=12)
ax.tick_params(axis='both')
x_steps = range(1, max(values_file2) + 1, 1)  # Steps of 1 from 0 to the max value
ax.set_xticks(x_steps)  # Set the ticks to these steps

plt.tight_layout()
plt.savefig("conf_vs_retrieval_raincloud_plot_600_400_px.pdf")
plt.show()
