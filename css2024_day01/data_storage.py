#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Start 13:45

Focusing on storing data

1. Lists
2. Dictionaries
3. Data Frame
"""

import pandas

file = pandas.read_csv("country_data.csv")

#print(file)

#age = file.Age

#age = file["Age"]

# age = [30, 25, 29, 46, 22]

#print(age)

# print(age[0])

# print(age[1])

# print(min(age))

# print(max(age))

# print(sum(age))

# print(len(age))

# avg = sum(age)/len(age)

# print(avg)


# g1 = "M"
# ge = "F"
# g3 = "M"

# gender = ["M","F","F"]

# c1 = "South Africa"
# c2 = "Lesotho"

# print(age[0:3])

#age.append(100)

# print(age)


"""
Start 15:15
"""

# age.insert(0,100)

# print(age)


"""
Dictionaries - key:value pairs

cat: "a cute animal"
"""

mammals = {"cat":"a cute animal", "lion":"king of the jungle", "elephant":"a giagatic herbivore"}

# print(mammals["cat"])

"""
Dat frames
"""

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
size_mm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits': fruits,
    'sizes': size_mm
    }

"""
df = dataframe
"""

import pandas as pd

df = pd.DataFrame(fruit_sizes)


# print(df)

# print(df['fruits'])

# print(df['sizes'])

# print(df['sizes'].min())

# print(df['sizes'].mean())

# print(df.describe())

# print(df[df["sizes"] > 10])

# print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, .00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)

print(df)

















