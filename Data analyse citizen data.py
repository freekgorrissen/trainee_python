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

def Versus(group_y, group_x):

    versus_y = dataset.groupby([group_y, group_x]).size()                                                           ##Make groups and count instances

    plt.bar(versus_y[1], versus_y[2], width =0.8)                                                                   ##Plot for group
    plt.xlabel(group_x)                                                                                             ## Some labels and titles below
    plt.ylabel(group_y)
    plt.title(group_y + " versus " + group_x)
    plt.show()
    return versus_y

print(Versus('occupation', 'education'))








