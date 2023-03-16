# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd
import json
import redis

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
load = redis.Redis(host='67.159.94.11', port=6379)
app = Dash(__name__, external_stylesheets=external_stylesheets)

metrics = json.loads(load.get("metrics").decode("utf-8"))

app.layout = html.Div([
    dcc.Interval(id='time',interval=10000),
    html.Div(id='output')
])

@app.callback(Output(component_id='output', component_property='children'),Input(component_id='time', component_property='n_intervals'))
def graph(n_intervals):
    load = redis.Redis(host='67.159.94.11', port=6379)
    metrics = json.loads(load.get("metrics").decode("utf-8"))
    data = json.loads(load.get("yg202-proj3-output").decode("utf-8"))
    current = metrics["timestamp"]
    df = pd.DataFrame({
        "CPU": data["CPU"][0],
        "CPU_Percent": data["CPU"][1]
    })

    df2 = pd.DataFrame({
        "Buffers":"virtual_memory-buffers",
        "result":data["buffers"]
    },index=[0])
    df3 = pd.DataFrame({
        "Cached":"virtual_memory-cached",
        "result":data["cached"]
    },index=[0])
    fig1 = px.bar(df, x="CPU", y="CPU_Percent")
    fig2 = px.bar(df2, x="Buffers",y="result")
    fig3 = px.bar(df3, x="Cached",y="result")
    return html.Div(children=[
    html.H1(children='CS401-Project3'),

    html.Div(children='''
        Monitoring Dashboard :P\
    '''),
    html.Div(children = current),

    dcc.Graph(
        id='CPU_Utilization',
        figure=fig1,
    ),

    dcc.Graph(
        id='Buffers',
        figure=fig2,
        style={"width":500}
    ),
    
    dcc.Graph(
        id='Cached',
        figure=fig3,
        style={"width":500}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True,port=31507,host="0.0.0.0")
