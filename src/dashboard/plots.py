import plotly.graph_objects as go


def create_scatter_geo(longitudes, latitudes):
    fig = go.Figure(
        data=go.Scattergeo(
            lon=longitudes,
            lat=latitudes,
            mode='markers',
            text='a'
        )
    )

    fig.update_layout(
        title='Real-time aircraft flying over Europe',
        geo_scope='europe',
        height=750,
        margin=dict(r=0, t=25, l=0, b=0),
    )

    return fig
