import dash

from src.callbacks import register_callbacks
from src.layout import get_layout


app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
app.layout = get_layout()
register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
