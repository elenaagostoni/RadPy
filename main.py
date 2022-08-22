import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd

df = pd.read_csv('data.csv', sep=';')

figs = make_subplots(rows=1, cols=2, specs=[[{"type": 'xy'}, {'type': 'domain'}]])

fig1 = px.bar(df, x='placeholder', y="dose", color="tag", barmode="stack", hover_name='source')
fig2 = px.pie(df, values='dose', names='source', color='tag', hover_name='source')
figs.update_xaxes(title_text="", range=[-2, 2], row=1, col=1)
figs.add_trace(fig1.data[0], row=1, col=1)
figs.add_trace(fig2.data[0], row=1, col=2)
figs.show()