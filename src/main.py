import dash
import dash_bootstrap_components as dbc

from src.dashboard.callbacks import register_callbacks
from src.dashboard.layout import get_layout


app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Europe flights",
    update_title="Updating flights...",
)
app.layout = get_layout()
register_callbacks(app)

if __name__ == "__main__":
    app.run_server(debug=True, dev_tools_silence_routes_logging=False)
