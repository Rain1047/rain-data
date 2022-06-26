import pandas as pd
import numpy as np
import math
import json
# matplotlib
import matplotlib.pyplot as plt
import datetime
import seaborn as sns
# plotly
import plotly.express as px
import plotly.graph_objects as go
import plotly 

def get_complete_plot():
    # import data
    complete_profile = pd.read_csv('./dashboardapp/static/data/starbucks/complete_profile.csv')
    # age
    female_age = complete_profile.query('gender == "F"').age.values
    male_age = complete_profile.query('gender == "M"').age.values
    female_age.sort()
    male_age.sort()
    # income
    female_income = complete_profile.query('gender == "F"').income.values
    male_income = complete_profile.query('gender == "M"').income.values
    female_income.sort()
    male_income.sort()
    # member year by gender
    female_member_year = complete_profile.query('gender == "F"').member_year.values
    male_member_year = complete_profile.query('gender == "M"').member_year.values
    female_member_year.sort()
    male_member_year.sort()

    #-------------------#
    # fig1
    #-------------------#
    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(
        x = male_age,
        name = 'male',
        marker_color = '#FFD700',
        opacity = 0.9
    ))
    fig1.add_trace(go.Histogram(
        x = female_age,
        name = 'female',
        marker_color = '#4682B4',
        opacity = 0.7
    ))
    # Overlay both histograms
    fig1.update_layout(
        title_text='Age Distribution', # title of plot
        xaxis_title_text='Age', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)
    
    #-------------------#
    # fig2
    #-------------------#
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(
        x = male_income,
        name = 'male',
        marker_color = '#EB89B5',
        opacity = 0.5
    ))
    fig2.add_trace(go.Histogram(
        x = female_income,
        name = 'female',
        marker_color = '#330C73',
        opacity = 0.5
    ))
    # Overlay both histograms
    fig2.update_layout(
        title_text='Income Distribution', # title of plot
        xaxis_title_text='Income', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)

    #-------------------#
    # fig3
    #-------------------#
    fig3 = go.Figure()
    fig3.add_trace(go.Histogram(
        x = male_member_year,
        name = 'male',
        marker_color = '#008B8B',
        opacity = 0.7
    ))
    fig3.add_trace(go.Histogram(
        x = female_member_year,
        name = 'female',
        marker_color = '#1E90FF',
        opacity = 0.7
    ))
    # Overlay both histograms
    fig3.update_layout(
        title_text='Member Join Date Distribution', # title of plot
        xaxis_title_text='Join Year', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)
    
    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return graph1JSON,graph2JSON,graph3JSON

def get_high_frequency_plot():
    # import data
    profile_new = pd.read_csv('./dashboardapp/static/data/starbucks/profile_new.csv')

    # age
    female_age = profile_new.query('gender == "F" & view_rate >=0.75 & complete_rate >= 0.5').age.values
    male_age = profile_new.query('gender == "M" & view_rate >=0.75 & complete_rate >= 0.5').age.values
    female_age.sort()
    male_age.sort()
    # income
    female_income = profile_new.query('gender == "F" & view_rate >=0.75 & complete_rate >= 0.5').income.values
    male_income = profile_new.query('gender == "M" & view_rate >=0.75 & complete_rate >= 0.5').income.values
    female_income.sort()
    male_income.sort()
    # member year by gender
    female_member_year = profile_new.query('gender == "F" & view_rate >=0.75 & complete_rate >= 0.5').member_year.values
    male_member_year = profile_new.query('gender == "M" & view_rate >=0.75 & complete_rate >= 0.5').member_year.values
    female_member_year.sort()
    male_member_year.sort()

    #-------------------#
    # fig1
    #-------------------#
    import plotly.graph_objects as go 

    fig1 = go.Figure()
    fig1.add_trace(go.Histogram(
        x = male_age,
        name = 'male',
        marker_color = '#FFD700',
        opacity = 0.9
    ))
    fig1.add_trace(go.Histogram(
        x = female_age,
        name = 'female',
        marker_color = '#4682B4',
        opacity = 0.7
    ))
    # Overlay both histograms
    fig1.update_layout(
        title_text='Age Distribution', # title of plot
        xaxis_title_text='Age', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)

    #-------------------#
    # fig2
    #-------------------#
    fig2 = go.Figure()
    fig2.add_trace(go.Histogram(
        x=male_income,
        name = 'male',
        marker_color = '#EB89B5',
        opacity = 0.5
    ))
    fig2.add_trace(go.Histogram(
        x = female_income,
        name = 'female',
        marker_color = '#330C73',
        opacity = 0.5
    ))
    # Overlay both histograms
    fig2.update_layout(
        title_text='Income Distribution', # title of plot
        xaxis_title_text='Income', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)

    #-------------------#
    # fig3
    #-------------------#
    fig3 = go.Figure()
    fig3.add_trace(go.Histogram(
        x = male_member_year,
        name = 'male',
        marker_color = '#008B8B',
        opacity = 0.7
    ))
    fig3.add_trace(go.Histogram(
        x = female_member_year,
        name = 'female',
        marker_color = '#1E90FF',
        opacity = 0.7
    ))
    # Overlay both histograms
    fig3.update_layout(
        title_text='Member Join Date Distribution', # title of plot
        xaxis_title_text='Join Year', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1, # gap between bars of the same location coordinates
        barmode='overlay',
        template="gridon",)

    graph1JSON = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    graph2JSON = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)
    graph3JSON = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

    return graph1JSON,graph2JSON,graph3JSON