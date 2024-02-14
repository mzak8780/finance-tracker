from dash import Dash, html, dcc
from . import year_dropdown
from . import month_dropdown
from . import category_dropdown
from . import bar_chart
import pandas as pd

def create_layout(app: Dash, data:pd.DataFrame) -> html.Div:
    return html.Div(
        className = 'app-div',
        children=[html.H1(app.title),
        html.Hr(), 
        html.Div(
            className = "dropdown-container",
            children = [
                year_dropdown.render(app, data),
                month_dropdown.render(app, data),
                category_dropdown.render(app, data),
            ],
        ),
        bar_chart.render(app, data)
    ],
)
