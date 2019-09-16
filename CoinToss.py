#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:00:56 2019

@author: DannySwift
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import time


def toss_coins(num_coins):
    ar = np.random.binomial(1, 0.5, num_coins)
    for i in range(1, len(ar)):
        ar[i] = ar[i - 1] + ar[i]
    df = pd.DataFrame(ar)
    return(df)


def main():
    coins = int(input("How many coins would you like to toss? "))
    while coins != 0:
        try:
            df = df.merge(toss_coins(coins) + df.iloc[-1], how='outer')
        except NameError:
            df = toss_coins(coins)
        df2 = df.copy()
        for i in range(1, len(df)):
            df2.iloc[i] = df.iloc[i] / (i + 1) * 100
        plt.ylim(0, 100)
        sns.lineplot(data=df2).set(ylabel='Percent Heads')
        plt.show()
        coins = int(input("How many more coins would you like to toss? "))

if __name__ == '__main__':
    main()