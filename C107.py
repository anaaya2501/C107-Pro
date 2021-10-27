import pandas as pd
import csv 
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
students_df = df.loc[df["student_id"]=="TRL_987"]
print(students_df.groupby("level")["attempt"].mean())

fig = go.Figure(go.Scatter(x = students_df.groupby("level")["attempt"].mean(),y = ["level1","level2","level3","level4"],orientation = "h"))
fig.show()