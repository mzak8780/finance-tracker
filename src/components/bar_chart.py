from dash import Dash, dcc, html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.express as px
from .configure_transactions import DataSchema

from . import ids

def render(app: Dash, data: pd.DataFrame) -> html.Div:

    @app.callback(
        Output(ids.BAR_CHART, "children"),
        [
            Input(ids.YEAR_DROPDOWN, "value"),
            Input(ids.MONTH_DROPDOWN, "value"),
            Input(ids.CATEGORIES_DROPDOWN, "value"),
        ]
    )
    def update_bar_chart(years: list[str], months: list[str], categories: list[str]) -> html.Div:
        filtered_data = data.query("Year in @years and Month in @months and Type in @categories")
        if filtered_data.shape[0] == 0:
            return html.Div("No data selected")

        def create_pivote_table() -> pd.DataFrame:
            pt = filtered_data.pivot_table(
                values = DataSchema.DEBIT,
                index = [DataSchema.TYPE],
                aggfunc="sum",
                fill_value = 0
            )
            return pt.reset_index().sort_values(DataSchema.DEBIT, ascending = False)

        fig = px.bar(
            create_pivote_table(),
            x=DataSchema.TYPE,
            y=DataSchema.DEBIT,
            color=DataSchema.TYPE
        )
        return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

    return html.Div(
        id=ids.BAR_CHART
    )
