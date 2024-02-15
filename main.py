from dash import Dash, html, dcc
from dash_bootstrap_components.themes import BOOTSTRAP
from src.components.layout import create_layout
from src.file_config.configure_file import configureFile

DATA_PATH = "./data/Transactions.csv"

def main() -> None:
    configured_file = configureFile(DATA_PATH)
    app = Dash(external_stylesheets=["https://codepen.io/chriddyp/pen/bWLwgP.css"])
    # app = Dash(__name__)
    app.title = "Financial Overview"
    app.layout = create_layout(app, configured_file)
    app.run()

if __name__ == "__main__":
    main()