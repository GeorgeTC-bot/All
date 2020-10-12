import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")

std_id = input("\nEnter Id: ")

std_df = df.loc[df["student_id"] == std_id]

print("\n")
print(std_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Bar(
            x=std_df.groupby("level")["attempt"].mean(),
            y=['Level 1', 'Level 2', 'Level 3', 'Level 4'],
            orientation='h'))

fig.show()
