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
df = px.data.tips()

# Functions
def open_browser():
    webbrowser.open_new('http://127.0.0.1:8050')


def create_app_ui():
    days = df['day'].unique()
    print(days)

    main_layout = html.Div(
        [
            dcc.Dropdown(id="dropdown", 
            options = [{'label':x, 'value':x} for x in days],
            value = 'Thur'),

            dcc.Graph(id="graph", figure=go.Figure())
        ]
    )
    return main_layout


@app.callback(
    Output("graph", "figure"),
    [
        Input("dropdown", "value")
    ]
)
def get_graph(day):
    display_df = df[df['day'] == day]
    figure = px.bar(display_df, x = 'sex', y = 'total_bill', color='smoker')

    # figure = px.scatter(df, x='total_bill', y='tip', color='sex')
    return figure


# Main flow of the project
def main():
    app.layout = create_app_ui()
    open_browser()
    app.run_server()


if __name__ == '__main__':
    main()