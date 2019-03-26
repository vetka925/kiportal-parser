#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 10:47:03 2019

@author: vetka
"""
import pandas as pd

result = []
for name in df['name']:
    i = 0
    for c in df[df.name == name]:
        if "Заявитель" in c:
            if not pd.isna(df[df.name == name][c].values[0]):
                i+=1
    result.append(i)
    