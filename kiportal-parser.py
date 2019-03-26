#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 17:37:18 2019

@author: vetka
"""
import requests
from bs4 import BeautifulSoup as BS
import pandas as pd

if  __name__ ==  "__main__" :

    df = pd.DataFrame()
    home = "https://kiportal.ru/reestr/reestry-sro/reestr-chlenov"
    url = 'https://kiportal.ru/reestr/reestry-sro/reestr-chlenov.html'
    pages = [home+'/'+str(i)+'.html' for i in range(2,124)]
    pages.append(url)

    tabs = {'tab-reestr',
            'tab-company',
            'tab-insurance',
            'tab-payment',
            'tab-complaints',
            'tab-checks',
            'tab-disciplinary',
            'tab-status'}
    members_links = {}
    member_info = {}

    for p in pages:
        r = requests.get(p)
        soup = BS(r.text
        t = soup.find('tbody')
        for a in t.findAll('tr'):
            name_link = a.findAll('a')[0]
            link = "https://kiportal.ru"+name_link['href']
            name = name_link.text
            print(name)
            members_links[name] = link

    for member in members_links:
        print(member)
        member_info = {}
        member_info['name'] = member
        r = requests.get(members_links[member])
        soup = BS(r.text)
        for t in tabs:
            tab = soup.find('div', {'id': t})
            if tab is not None:
                if t in ['tab-company', 'tab-status']:
                    for h in tab.findAll('div'):
                        if h is not None:
                            try:
                                member_info[h.find('h3').text] = h.text
                            except AttributeError:
                                continue
                else:
                    for info in tab.findAll('tr'):

                        if info.findAll('td')[0].text in member_info:

                            member_info[info.findAll('td')[0].text] = info.findAll('td')[1].text
        df = df.append(member_info, ignore_index=True)

    df.to_csv('data/kiportal-dataframe.csv')
