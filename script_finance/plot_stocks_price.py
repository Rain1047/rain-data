import plotly.express as px 
import json, plotly 
import pandas as pd
import requests

#Description
#Price to earnings ratio, based on trailing twelve month as reported earnings. Current PE is estimated from latest reported earnings and current market price. Source: Robert Shiller and his book Irrational Exuberance for historic S&P 500 PE Ratio.
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

def get_price_plot():
    # sp500
    sp500_price_df = pd.read_csv('./dashboardapp/static/data/finance/us_sp500_price.csv').head(120)
    fig1 = px.line(sp500_price_df, x=sp500_price_df['Date'], y=sp500_price_df['sp500 price'], title='SP500 Price By Month (Recent 10 years)')
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

    # cpi
    consumer_price_df = pd.read_csv('./dashboardapp/static/data/finance/us_cpi_price.csv').head(120)
    fig2 = px.line(consumer_price_df, x=consumer_price_df['time'], y=consumer_price_df['consumer_price'], title='Consumer Price By Month (Recent 10 years)')
    fig2.update_xaxes(
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
    fig2.update_layout(
        template="gridon"
    )

    # inflation rate
    inflation_df = pd.read_csv('./dashboardapp/static/data/finance/us_inflation_rate.csv').head(120)
    fig3 = px.line(inflation_df, x=inflation_df['time'], y=inflation_df['inflation_rate'], title='Inflation Rate By Month (Recent 10 years)')
    fig3.update_xaxes(
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
    fig3.update_layout(
        template="gridon"
    )




    # sp500
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    # cpi
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    # inflation rate
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph1JSON, graph2JSON, graph3JSON
    
# sp500_df = pd.read_csv('./dashboardapp/static/data/finance/us_sp500_price.csv')