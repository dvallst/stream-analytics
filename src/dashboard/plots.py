import plotly.graph_objects as go


def create_geo_map(latitudes, longitudes, flight_info):
    """
    Create European geographic map provided by latitude/longitude pairs

    :param latitudes: Pandas series of latitudes in ellipsoidal coordinates (WGS-84) and decimal degrees
    :param longitudes: Pandas series of longitudes in ellipsoidal coordinates (WGS-84) and decimal degrees
    :param flight_info: Pandas series of flight information
    :return: Figure: European map with flights
    """
    fig = go.Figure(data=go.Scattergeo(lat=latitudes, lon=longitudes, mode="markers", text=flight_info))

    fig.update_layout(
        title="All aircraft flying",
        geo_scope="europe",
        width=750,
        height=800,
        margin=dict(r=0, t=25, l=0, b=0),
    )

    return fig
