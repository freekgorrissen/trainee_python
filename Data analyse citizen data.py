#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Julian
#
# Created:     14/09/2021
# Copyright:   (c) Julian 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#from scipy import ttest_ind as tt
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
import pandas as pd

dataset = pd.read_csv('C:/Users/Julian/Documents/Traineeship Projecten/Python opdracht 2e week/CSV van drive/102_cleaned_header.csv')

def SalaryBy(group):
    salary_per = dataset.groupby([group]).mean()                                                                    ## Find out how group and salary compare
    salary_per_std = dataset.groupby([group]).std()                                                                 ## Determine the standard deviation
    salary_per = salary_per.reset_index()                                                                           ## Reset index so plt can read all of the columns

    plt.bar(salary_per[group], salary_per['salary'], width =0.8, yerr = salary_per_std['salary'], capsize = 10)     ##Plot salary for group
    plt.xlabel(group)                                                                                               ## Some labels and titles below
    plt.ylabel("Salary")
    plt.title("Average salary by " + group)
    plt.show()


#SalaryBy('education')

def Versus_graph(group_y, group_x):
    versus_y = dataset.groupby([group_y, group_x]).size()                                                           ##Make groups and count instances

    versus_y.unstack(0).plot.bar()
    plt.xlabel(group_x)                                                                                             ## Some labels and titles below
    plt.ylabel("#")
    plt.title(group_y + " and " + group_x)
    plt.show()
    #return versus_y

#Versus_graph('sex', 'number_of_cars_owned')                                                                        ##Define what you want to count first, then define what you want your groups on the x-axis to be


def Versus_stats(group_y, group_x):
    versus_y =
    #result = tt.
    return versus_y

print(Versus_stats('sex', 'salary'))


