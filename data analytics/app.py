# Importing the libraries
import webbrowser 
import dash
from dash import html
from dash.dependencies import Input, Output
import dash_core_components as dcc

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


# Main flow of the project
def main():
    app.layout = create_app_ui()
    open_browser()
    app.run_server()


if __name__ == '__main__':
    main()