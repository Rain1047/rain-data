from dashboardapp import app
from flask import render_template
import pandas as pd
import json, plotly
import sqlite3 as sql
# from script_finance.wrangling import data_wrangle
import plotly.express as px
# finance script
from script_finance.nasdaq_pe_ratio import get_nasdaq_pe_ratio
from script_finance.sp500_returns import get_sp500_returns
from script_finance.plot_stocks_price import get_price_plot
from script_finance.plot_index import get_mmth_plot
# starbucks script
from script_starbucks.starbucks_analysis import get_complete_plot, get_high_frequency_plot

# app = Flask(__name__)

# home page
@app.route('/')
def index():  
  return render_template('index.html')



#----------------------#
# bilibili project
#----------------------#
@app.route('/bilibili-main')
def get_bilibili():
  return render_template('project-bilibili-main.html')

#----------------------#
# starbucks project
#----------------------#
@app.route('/starbucks-main')
def starbuucks_main():
  return render_template('project-starbucks-main.html')

@app.route('/starbucks-main/starbucks-analysis')
def starbuucks_analysis():
  graph1json, graph2json, graph3json = get_complete_plot()
  graph4json, graph5json, graph6json= get_high_frequency_plot()
  return render_template(
    'project-starbucks-analysis.html', 
    graph1json= graph1json, 
    graph2json= graph2json, 
    graph3json= graph3json,
    graph4json= graph4json, 
    graph5json= graph5json, 
    graph6json= graph6json)

#----------------------#
# netflix project
#----------------------#
@app.route('/netflix-main')
def get_netflix():
  return render_template('project-netflix-main.html')

#----------------------#
# fiance project
#----------------------#
@app.route('/finance-main')
def get_finance():
  graph1json, graph2json, graph3json = get_price_plot()
  graphJSON_mmth = get_mmth_plot()
  return render_template(
    'project-finance-main.html',
    # sp500 price 10years
    graphjson_sp500 = graph1json,
    graphjson_cpi = graph2json,
    graphjson_inflation_rate = graph3json,
    graphjson_mmth = graphJSON_mmth)

@app.route('/finance-main/finance-article/score-system-review')
def get_article_1():
  return render_template('score_system_review_1.html')

@app.route('/finance-main/finance-article/pyechart-demo')
def get_pyechart_demo():
  return render_template('sz.300059.html')

#----------------------#
# crypto project
#----------------------#
@app.route('/crypto-main')
def get_crypto():
  # graph1json = get_sp500_plot()
  return render_template(
    'project-crypto-main.html',
    # sp500 price 10years
    # graph1json = graph1json
    )

@app.route('/crypto-main/bitcoin')
def btc_list():
  database = "dashboardapp/static/data/crypto/crypto.db"
  con = sql.connect(database)
  con.row_factory = sql.Row
  
  cur = con.cursor()
  cur.execute("select * from bitcoin")
  
  rows = cur.fetchall()
  return render_template("project-crypto-btc.html", rows = rows)