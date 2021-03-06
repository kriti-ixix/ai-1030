# Importing the libraries
import webbrowser 
import dash
from dash import html
from dash.dependencies import Input, Output
from dash import dcc

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Global variables
app = dash.Dash()


# Functions
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050')


def create_app_ui():
    main_layout = html.Div(
        [
            html.H1(id="main_title", children="My Project"),

            html.Button(id="button", children="Click me", n_clicks=0),

            html.Hr(),

            dcc.Dropdown(id="dropdown", 
            options = [ {'label': 'Bar Graph', 'value':'bar'}, {'label':'Line Graph', 'value':'line'} ],
            value = 'line'),

            dcc.Graph(id="graph", figure=go.Figure())
        ]
    )
    return main_layout


@app.callback(
    Output("main_title", "children"),
    [
        Input("button", "n_clicks")
    ]
)
def change_text(n_clicks):
    return f"Button clicked {n_clicks} times"


@app.callback(
    Output("graph", "figure"),
    [
        Input("dropdown", "value")
    ]
)
def update_graph(value):
    data = [["ABC", 10], ["XYZ", 15], ["PQR", 25], ["JKL", 50]]
    df = pd.DataFrame(data, columns=['Name', 'Age'])
    figure = None

    if value == 'line':
        figure = px.line(df, x = 'Name', y='Age')
    else:
        figure = px.bar(df, x = 'Name', y = 'Age')

    return figure


# Main flow of the project
def main():
    app.layout = create_app_ui()
    open_browser()
    app.run_server()


if __name__ == '__main__':
    main()