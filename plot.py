#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:10:21 2019

@author: vetka
"""

from plotly.offline import download_plotlyjs, plot
import plotly
import plotly.graph_objs as go

final = pd.read_csv('data/dfforrates.csv')

trace0 = go.Bar(
    y=[ len(final[final['Score'] == i]) for i in final['Score']],
    x=final['Score'],
    name='Score'
)

data = [trace0]
layout = {'title': 'Статистика рейтингов'}

# cоздаем объект Figure и визуализируем его
fig = go.Figure(data=data, layout=layout)
iplot(fig, show_link=False)

plotly.offline.plot(fig, filename='ki-ratings.html', show_link=False)
