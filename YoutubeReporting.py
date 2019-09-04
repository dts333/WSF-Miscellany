#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:40:20 2019

@author: DannySwift
"""

import googleapiclient
import os
import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns

from YoutubeConfig import VIDSTATS, VIDSTATSTITLES, CHANNELSTATS, DATA_DIRECTORY

def load_data(directory):
    data = pd.DataFrame(columns=['date', 'video_title'])
    files = os.listdir(directory)
    print(files)
    for file in files:
        for stat in VIDSTATSTITLES:
            if re.search('.*chart_{}.csv'.format(stat), file):
                data = data.merge(pd.read_csv(directory + os.sep + file), 
                                  how='outer', on=['date', 'video_title'])
        if re.search('.*VidPub.csv', file):
            dates = pd.read_csv(directory + os.sep + file)
    
    print(data.head())
    return data, dates

def graph_vid(df, dates, var):
    g = sns.lineplot(x='date', y=var, data=df, hue='video_title')
    for _, d in dates.iterrows():
        g.axvline(d['date'], label=d['name'])
    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)


def main():
    directory = input("Enter the folder containing the reporting data: ")
    directory = DATA_DIRECTORY + os.sep + directory
    data, dates = load_data(directory)
    for var in VIDSTATS:
        graph_vid(data, dates, var)


if __name__ == '__main__':
    main()