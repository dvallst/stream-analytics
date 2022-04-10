import dash

from src.dashboard.callbacks import register_callbacks
from src.dashboard.layout import get_layout


app = dash.Dash(
    __name__,
    external_stylesheets=['https://cdnjs.cloudflare.com/ajax/libs/skeleton/2.0.4/skeleton.min.css']
)
app.layout = get_layout()
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
