import plotly.express as px 
import json, plotly 
import pandas as pd
import requests

def get_nasdaq_pe_ratio():
    url = 'https://data.nasdaq.com/api/v3/datasets/MULTPL/SHILLER_PE_RATIO_MONTH.json'
    data_list = requests.get(url).json()['dataset']['data']
    xray = []
    yray = []
    for data in data_list:
        xray.append(data[0])
        yray.append(data[1])
    # print(xray[:5])
    # print(yray[:5])
    df = pd.DataFrame({
        'Date':xray,
        'P/E Ratio':yray
    })

    fig = px.line(df, x='Date', y='P/E Ratio', title='Nasdaq P/E Ratio By Month')
    fig.update_xaxes(
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
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON
# print(df)