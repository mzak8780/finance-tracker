from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
from . import ids
from ..file_config.configure_file import DataSchema

def render(app: Dash, data: pd.DataFrame) -> html.Div:
    all_categories: list[str] = data[DataSchema.TYPE]
    unique_categories = sorted(set(all_categories))

    @app.callback(
        Output(ids.CATEGORIES_DROPDOWN, "value"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.SELECT_ALL_CATEGORIES_BUTTON, "n_clicks")
        ]
    )   
    def update_categories(years: list[str], months: list[str],  _: int) -> list[str]:
       filtered_data = data.query("Year in @years and Month in @months")
       print(set(filtered_data[DataSchema.TYPE]))
       return sorted(set(filtered_data[DataSchema.TYPE]))

    return html.Div(
        children=[
            html.H6("Category"),
            dcc.Dropdown(
                id=ids.CATEGORIES_DROPDOWN,
                options = [{"label": category, "value": category} for category in unique_categories],
                value=unique_categories,
                multi=True
            ),
            html.Button(
                className="dropdown-button",
                children=["Select All"],
                id=ids.SELECT_ALL_CATEGORIES_BUTTON,
                n_clicks=0,
            )
        ]
    )
