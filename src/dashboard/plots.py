import plotly.graph_objects as go


def create_scatter_geo(latitudes, longitudes, flight_info):
    """

    :param latitudes:
    :param longitudes:
    :param flight_info:
    :return: Figure: Europe map with flights
    """
    fig = go.Figure(
        data=go.Scattergeo(
            lat=latitudes,
            lon=longitudes,
            mode='markers',
            text=flight_info
        )
    )

    fig.update_layout(
        title='All aircraft flying',
        geo_scope='europe',
        width=750,
        height=800,
        margin=dict(r=0, t=25, l=0, b=0),
    )

    return fig
