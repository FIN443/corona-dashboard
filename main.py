import dash
from dash import dcc
from dash import html
import plotly.express as px
from data import countries_df, totals_df
from builders import make_table

stylesheets = [
    "https://cdn.jsdelivr.net/npm/reset-css@5.0.1/reset.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=stylesheets)

bubble_map = px.scatter_geo(
    countries_df,
    size="Confirmed",
    size_max=40,
    hover_name="Country_Region",
    locations="Country_Region",
    locationmode="country names",
    color="Confirmed",
    title="Confirmed By Country",
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Oryel,
    projection="natural earth",
    hover_data={
        "Confirmed": ":,.0f",
        "Deaths": ":,.0f",
        "Recovered": ":,.0f",
        "Country_Region": False,
    },
)
bubble_map.update_layout(margin=dict(l=0, r=0, t=40, b=0))

bars_gragh = px.bar(
    totals_df,
    x="condition",
    y="count",
    template="plotly_dark",
    title="Total Global Cases",
    hover_data={
        "count": ":,",
        "condition": False,
    },
)
bars_gragh.update_layout(xaxis=dict(title="Condition"), yaxis=dict(title="Count"))

app.layout = html.Div(
    style={
        "minHeight": "100vh",
        "backgroundColor": "#111111",
        "color": "white",
        "fontFamily": "Open Sans, sans-serif",
    },
    children=[
        html.Header(
            style={
                "textAlign": "center",
                "paddingTop": "50px",
                "marginBottom": 100,
            },
            children=[html.H1("Corona Dashboard", style={"fontSize": 40})],
        ),
        html.Div(
            children=[
                html.Div(children=[dcc.Graph(figure=bubble_map)]),
                html.Div(children=[make_table(countries_df)]),
            ]
        ),
        html.Div(
            children=[
                html.Div(children=[dcc.Graph(figure=bars_gragh)]),
            ]
        ),
    ],
)


if __name__ == "__main__":
    app.run_server(debug=True)
