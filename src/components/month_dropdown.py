from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from . import ids
from .configure_transactions import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_months: list[str] = data[DataSchema.MONTH]
    unique_months = sorted(set(all_months), key=int)

    @app.callback(
        Output(ids.MONTH_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_MONTHS_BUTTON, "n_clicks")
        ]
    )   
    def update_months(years: list[str], _: int) -> list[str]:
       filtered_data = data.query("Year in @years")
       print(set(filtered_data[DataSchema.MONTH]))
       return sorted(set(filtered_data[DataSchema.MONTH]))

    return html.Div(
        children=[
            html.H6("Month"),
            dcc.Dropdown(
                id=ids.MONTH_DROPDOWN,
                options = [{"label": month, "value": month} for month in unique_months],
                value=unique_months,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_MONTHS_BUTTON,
                n_clicks=0,
            )
        ]
    )
