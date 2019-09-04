#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:40:20 2019

@author: DannySwift
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def graph_apv(df, dates):
    g = sns.lineplot(x='date', y='average_percentage_viewed', data=apv, hue='video_title')
    for _, d in dates.iterrow():
        g.axvline(d['date'], label=d['name'])
    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)