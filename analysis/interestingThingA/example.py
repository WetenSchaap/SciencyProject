"""
Creation date: 2022-11-08
Author: Piet Swinkels

example.py

This notebook does nothing and is just an example.
"""

#%% Load packages
# Always a strong start
import sys
import pathlib

import math
import numpy as np
import pandas as pd
import scipy

import matplotlib.pyplot as plt
import tol_colors as tc
import pjmsplotting as pp

#%% Load data
# Get data into pd.DataFrame
datafile = pathlib.Path(r"/path/to/raw/data.csv")
df = pd.read_csv(datafile)

#%% Do analysis
# Do the analysis step
df.dosomething()

#%% plot
# Plot data

fig,ax = plt.subplots(1,1)
cset = tc.tol_cset('high-contrast')

ax.plot(
    df["x"],
    df["y"],
    c=cset[1]
)

pp.squarify(fig)

#%% save
# Save the plot
fig.savefig("tada.png", bbox_inches='tight')