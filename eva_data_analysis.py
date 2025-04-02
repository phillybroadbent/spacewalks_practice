import json
import csv
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd

# https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding="utf-8")
output_file = open('./eva-data.csv','w', encoding="utf-8")
graph_file = './cumulative_eva_graph.png'  

# Read the data from a JSON file into a pandas dataframe
eva_df = pd.read_json(input_file, convert_dates=['date'])
eva_df['eva'] = eva_df['eva'].astype(float)

# Clean the data by removing any incomplete rows and sort by date
eva_df.dropna(axis=0, inplace=True)
eva_df.sort_values('date', inplace=True)

# Save dataframe to CSV for later analysis
eva_df.to_csv(output_file, index=False)

eva_df['duration_hours'] = eva_df['duration'].str.plit(":").apply(lambda x: int(x[0]) + int(x[1]/60))
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

# Plot cumulative time spent in space over the years
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

