import datetime
import glob
import logging
import math
import os
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot

logger = logging.getLogger(__name__)

count = 100


def plot1d(X, Y):
    trace1 = go.Scatter(
        x=X,
        y=Y
    )

    data = [trace1]
    layout = go.Layout(

        height=600,

        margin=go.layout.Margin(
            l=35,
            r=0,
            b=0,
            t=5

        ),

        plot_bgcolor='rgba(73,80,87,0.1)',
        xaxis=dict(
            title='X Axis',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            ),
            autorange=True
        ),
        yaxis=dict(
            title='Y Axis',

            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            ),
            autorange=True
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    # logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div


def plotscatter(X, Y):
    trace1 = go.Scatter(
        x=X,
        y=Y,
        mode='markers', name='points',
        marker=dict(color='rgb(0,0,0)', size=2, opacity=0.4)
    )

    data = [trace1]
    layout = go.Layout(


        margin=go.layout.Margin(
            l=35,
            r=0,
            b=0,
            t=5

        ),

        plot_bgcolor='rgba(73,80,87,0.1)',
        xaxis=dict(
            title='X Axis',
            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            ),
            autorange=True
        ),
        yaxis=dict(
            title='Y Axis',

            titlefont=dict(
                family='Courier New, monospace',
                size=18,
                color='#7f7f7f'
            ),
            autorange=True
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    # logger.info("Plotting number of points {}.".format(len(x_data)))
    return plot_div


def live_plot_get_x_y_data():
    """
    Generates normal distributed 2D points
    Numer of points depends on the real time seconds.
    """
    global count
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # data_files = glob.glob(current_dir + '/data/scan*_Iq.txt')

    series = pd.read_csv(current_dir + '/data/monthly-sunspots.csv')
    Y = series['Sunspots']
    y_ = []
    if count < len(Y):

        for i in range(0, count, 1):
            y_.append(Y[i])
    else:
        count = 0
    X = np.linspace(0, len(y_), num=len(y_))
    # print(X[0:10])
    count = count + 100

    return X, y_


def live_plot_get_data():
    """
    Data to generate the first plot
    """
    x, y = live_plot_get_x_y_data()
    data = dict(
        x=x, y=y, mode='lines', name='points'
    )
    return data


def live_plot_get_data_serialized():
    """
    Data to generate the updated plot.
    It will serialized by the Django view
    """
    x, y = live_plot_get_x_y_data()
    data = dict(
        x=x.tolist(), y=y, mode='lines', name='points'
    )
    return data


def plotLive():
    # trace = go.Scatter(live_plot_get_data())

    data = live_plot_get_data_serialized()

    layout = go.Layout(
        title="Moving  Plot",
        # autosize=False,
        # width=900,
        # height=500,
        height=600,

        xaxis=dict(
            autorange=True
        ),
        # yaxis=dict(
        #    autorange=True
        # )
    )
    fig = go.Figure(data=data, layout=layout)
    plot_div = plot(fig, output_type='div', include_plotlyjs=False)
    return plot_div
