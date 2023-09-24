"""
This script uses functions from lib.py to generate a brief analysis of a
dataset and save a data viszualization of the data
"""
import pandas as pd 
from source import lib 
dt= pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
# Print dataset info
lib.print_ds_info(dt)
# view and save graph
lib.view_data_vis(dt)
lib.safe_data_vis2(dt)

#Print descriptive statistics of just one variable.
selected=dt.iloc[:,3]

lib.print_min(selected)
