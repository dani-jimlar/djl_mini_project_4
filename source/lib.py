"""
This fun prints descriptive analytics of a data set
"""

import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt

def print_ds_info(data):
    """
    parameter:data
    uses data.columns and describe() to print descriptive info of dataset
    """
    print("The variables in this data set are the following:",list(data.columns))
    print("The variables behave as follows:", data.describe())


def print_min(my_var):
    return "The min is " + str(my_var.min().round(2))

def print_mean(my_var):
    return "The mean is " + str(my_var.mean().round(2))

def print_median(my_var):
    return "The median is " + str(my_var.median())

def print_max(my_var):
    return "The max is " + str(my_var.max())

def print_1_qt(my_var):
    print("The first quantile is ",my_var.quantile(0.25)())

def print_3_qt(my_var):
    print("The third quantile is ",my_var.quantile(0.75)())


def view_data_vis(data):
    """this fun generates a simple plot of the data set"""
    plt.figure(figsize=(10, 12))
    plt.bar(data["descrip"], data["sexostt"])
    plt.title("Number of inmates by age group in Mexican prisons in 2021")
    plt.xlabel("Age group")
    plt.ylabel("Number of inmates")
    plt.legend()
    plt.tight_layout()
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.show()


def safe_data_vis2(data):
    plt.figure(figsize=(10, 12))
    plt.bar(data["descrip"], data["sexostt"])
    plt.title("Number of inmates by age group in Mexican prisons in 2021")
    plt.xlabel("Age group")
    plt.ylabel("Number of inmates")
    plt.legend()
    plt.tight_layout()
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)
    plt.savefig('source/bar_plot2.png', dpi=300, bbox_inches='tight')    

if __name__ == "__main__":
    #dir=os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'source'))
    #sys.path.append(dir)
    # Read the CSV file
    my_data = pd.read_csv("source/imp_edos_2.csv", encoding="ISO-8859-1")
    # Print dataset info
    #print_ds_info(my_data)
    safe_data_vis2(my_data)
    selected=my_data.iloc[:,3]
    # generate graph
    