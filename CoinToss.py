#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:00:56 2019

@author: DannySwift
"""

import matplotlib.animation
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


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

def main2():
    num_coins = int(input("How many coins are there? "))
    heads = int(input("How many are heads up? "))
    coins = np.zeros(heads) + 1
    coins = np.append(coins, np.zeros(num_coins - heads))
    history = [coins.sum()]
    flip = int(input("How many would you like to flip? "))
    tosses = int(input("How many times? "))
    tosses_per_frame = int(input("How many tosses per frame? "))
    for toss in range(tosses):
        ar = np.random.binomial(1, 0.5, flip)
        which_coins = np.random.choice(num_coins, size=flip, replace=False)
        for i in range(flip):
            coins[which_coins[i]] = ar[i]
        history.append(coins.sum())
    df = pd.DataFrame(history)
    
    fig = plt.figure()
    plt.ylim(0, num_coins)
    plt.xlim(0, tosses)
    plt.ylabel('Heads')
    plt.xlabel('Toss')
    
    def animate(i):
        p = sns.lineplot(data=df[:i * tosses_per_frame], legend=False)
        plt.setp(p.lines, color='r')
    ani = matplotlib.animation.FuncAnimation(fig, animate, 
                                             frames=int(tosses / tosses_per_frame) + 2)
    plt.show()

if __name__ == '__main__':
    main2()