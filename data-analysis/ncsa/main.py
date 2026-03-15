import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
pio.templates.default= "plotly_white"

netflix_data = pd.read_csv("netflix_content.csv")
netflix_data['Hours Viewed'] = netflix_data['Hours Viewed'].replace(',', '', regex=True).astype(float)

print(netflix_data.head())
