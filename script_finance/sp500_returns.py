import pandas as pd
import numpy as np
import requests, json
import plotly
import plotly.express as px 
import plotly.graph_objects as go 

def get_sp500_returns():
    url = 'https://data.nasdaq.com/api/v3/datasets/MULTPL/SP500_REAL_PRICE_MONTH.json?api_key=U7-3C3oT69mUDH7-F_VW'
    nasdaq_json = requests.get(url).json()['dataset']['data']

    time_list = []
    price_list = []
    rate_list = []
    nasdaq_len = len(nasdaq_json)
    for i in range(0,nasdaq_len,2):
            time_list.append(nasdaq_json[i][0])
            price_list.append(nasdaq_json[i][1])

    # 计算百分率
    price_arr = np.array(price_list)
    rate_arr = np.diff(price_arr)/price_arr[:-1]
    time_len = len(time_list)
    sp500_returns_rate = pd.DataFrame({
        'Date': time_list[:time_len-1],
        'Rate': rate_arr})

    sp500_returns_rate = sp500_returns_rate.head(192)
    sp_sub_1 = sp500_returns_rate[sp500_returns_rate.Rate >= 0]
    sp_sub_2 = sp500_returns_rate[sp500_returns_rate.Rate < 0]

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x = sp_sub_1.Date,
        y = sp_sub_1.Rate,
        marker_color = 'crimson',
        name = 'Rate > 0'
    ))
    fig.add_trace(go.Bar(
        x = sp_sub_2.Date,
        y = sp_sub_2.Rate,
        marker_color = 'lightslategrey',
        name = 'Rate < 0'
    ))
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON