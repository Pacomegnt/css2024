#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 23:26:13 2024

@author: pacome
"""

import pandas

# data 1
file = pandas.read_csv("country_data.csv")

# data 2
#file = pandas.read_csv("diab_data.csv")

# data 3
# column_names = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N"]
# file = pandas.read_csv("housing_data.csv", header=(None), names=column_names)


# data 4
#file = pandas.read_csv("insurance_data.csv", skiprows=5)

# data 
#file = pandas.read_csv("iris.csv")

print()
print(file)
print()
print(file.info())
print()
print(file.describe())

