# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 05:50:55 2022

@author: HP
"""
# importing pandas library
import pandas as pd
import numpy as np
# import matplotlib library
import matplotlib.pyplot as plt


def read_file(filename):
    """
    The function read_file read the file into dataframes

    """
    data = pd.read_excel(filename)

# transposing the data and stored in variable datatranspose

    datatranspose = data.set_index('Country Name').transpose()
    return data, datatranspose


# Setting a dataframe of countries to plot bar graph
country_list1 = ['China', 'United Kingdom', 'India', 'Italy', 'Pakistan']
# Setting a dataframe of countries to line graph
country_list2 = ['India', 'Pakistan', 'Saudi Arabia',
                 'Australia', 'Bangladesh', 'France']
"""
The function is used to filter the countries to plot the bar graph  from the dataframe
 
"""


def filter_bar_data(data):
    data = data[['Country Name', 'Indicator Name',
                 '1995', '2000', '2005', '2010', '2015']]
    data = data[(data["Country Name"] == "China") |
                (data["Country Name"] == "United Kingdom") |
                (data["Country Name"] == "India") |
                (data["Country Name"] == "Italy") |
                (data["Country Name"] == "Pakistan")]

    return data
    """
    
    The function is used to filter the countries to plot the line graph  from the dataframe
 
    """


def filter_line_plot(data):
    data = data[['Country Name', 'Indicator Name',
                 '1995', '2000', '2005', '2010', '2015']]
    data = data[(data["Country Name"] == "India") |
                (data["Country Name"] == "Pakistan") |
                (data["Country Name"] == "Saudi Arabia") |
                (data["Country Name"] == "Australia") |
                (data["Country Name"] == "Bangladesh") |
                (data["Country Name"] == "France")]
    return data


def barplot(data, label1, label2):
    """
    This function is used to plot a bar graph of Energy use and greenhouse gas emission
    where the y axis is showing differnt countries 

    """

    plt.figure(figsize=(30, 20))
    ax = plt.subplot(1, 1, 1)
    x = np.arange(5)
    width = 0.2

    bar1 = ax.bar(x, data["1995"], width, label=1995)
    bar2 = ax.bar(x+width, data["2000"], width, label=2000)
    bar3 = ax.bar(x+width*2, data["2005"], width, label=2005)
    bar4 = ax.bar(x+width*3, data["2010"], width, label=2010)

    ax.set_xlabel("Country Names", fontsize=35, c='black')
    ax.set_ylabel(label1, fontsize=35, c='black')
    ax.set_title(label2, fontsize=40)
    ax.set_xticks(x, country_list1, fontsize=30, rotation=90)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    ax.legend(fontsize=30)

    ax.bar_label(bar1, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar2, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar3, padding=2, rotation=90, fontsize=18)
    ax.bar_label(bar4, padding=2, rotation=90, fontsize=18)
    plt.show()


def line_plot(data, label1, label2):
    """
    This function is used to plot a line graph of Population growth and Urban Population.
    The x axis is showing different years

    """

    plt.figure(figsize=(25, 10))
    dd = data.set_index('Country Name')
    tran = dd.transpose()
    tran = tran.drop(index=['Indicator Name'])
    for i in range(len(country_list2)):
        plt.plot(tran.index, tran[country_list2[i]],
                 label=country_list2[i], linestyle='dashed', linewidth='3')

    plt.title(label2, size=25)
    plt.xlabel("Years", size=25, c='black')
    plt.ylabel(label1, size=20, c='black')
    plt.xticks(rotation=90, fontsize=25)
    plt.tick_params(axis='x', colors='black')
    plt.tick_params(axis='y', colors='black')
    plt.legend(fontsize=16)
    plt.show()


def greenhouse_data_mean():
    """
    This function is used to calculate the mean of greenhouse gas emission of the selected countries
   """

    data1, data2 = read_file(
        "C:/Users/HP/Documents/fname/greenhouse gas emission.py.xls")
    df = data1.set_index("Country Name")
    transpose = df.transpose()
    transpose = df.transpose()
    transpose = transpose.drop(index='Indicator Name')
    transpose = transpose.drop(index='Country Code')
    transpose = transpose.drop(index='Indicator Code')
    cleaned_data = transpose.fillna(0)
    mean = cleaned_data[["China", "United Kingdom",
                         "India", "Italy", "Pakistan"]].mean()

    return mean


# we are reading the data from excel for bar graph by giving the path.
Energy_data, Energy_data1 = read_file(
    "C:/Users/HP/Documents/fname/Energy use.xls")
Energy_data = filter_bar_data(Energy_data)
Greenhouse_data, Greenhouse_data1 = read_file(
    "C:/Users/HP/Documents/fname/greenhouse gas emission.py.xls")
Greenhouse_data = filter_bar_data(Greenhouse_data)

# we are reading the data from excel for line graph by giving the path.
Population_data, Population_data1 = read_file(
    "C:/Users/HP/Documents/fname/Population growth.xls")
Population_data = filter_line_plot(Population_data)
Urban_pop_data, Urban_pop_data1 = read_file(
    "C:/Users/HP/Documents/fname/urban population.xls")
Urban_pop_data = filter_line_plot(Urban_pop_data)

# plotting the bar graph of energy use and greenhouse gas emission data"
barplot(Energy_data, "Energy Use data (kg of oil equivalent per capita)", "Energy Use")
barplot(Greenhouse_data, "Total greenhouse gas emission(kg of oil equivalent per capita)",
        "Total greenhouse gas emission")

# plotting the line graph of population growth and urban population data
line_plot(Population_data, "Population growth", "Population growth (annual %)")
line_plot(Urban_pop_data, "Urban population (% of total population)",
          "Urban population")

# function to return the mean of greenhouse gas emission
mean = greenhouse_data_mean()
mean = mean.to_csv("mean_of_greenhouse_gas.csv")
