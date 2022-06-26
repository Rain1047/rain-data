import plotly.express as px 
import json, plotly 
import pandas as pd
import requests


def get_mmth_plot():
    mmth_price_df = pd.read_csv('./dashboardapp/static/data/finance/us_mmth.csv', skiprows=lambda x: x > 0 and x % 7 != 0)
    fig1 = px.line(mmth_price_df, x=mmth_price_df['datetime'], y=mmth_price_df['close'], title='MMTH Price By Week')
    fig1.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="month", stepmode="backward"),
            dict(count=6, label="6m", step="month", stepmode="backward"),
            dict(count=1, label="YTD", step="year", stepmode="todate"),
            dict(count=1, label="1y", step="year", stepmode="backward"),
            dict(count=4, label="4y", step="year", stepmode="backward"),
            dict(step="all")
            ])
        )
    )
    fig1.update_layout(
        template="gridon"
    )
    graphJSON_mmth = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON_mmth