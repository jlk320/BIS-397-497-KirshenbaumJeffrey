#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:49:31 2021

@author: jeffreykirshenbaum
"""


#Reading in "yellow_tripdata_2019-06.csv"

import pandas as pd
yellow_2019 = pd.read_csv("yellow_tripdata_2019-06.csv")

yellow_2019

#Rounding to 5 decimal places to make summary statistics easier to work with 
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#Looking at variables 

yellow_2019.columns

#Getting to know what type of data we have

yellow_2019.dtypes

yellow_2019['tpep_pickup_datetime'].head()


#Converting pickup and dropoff times from objects to date/time format

yellow_2019['pickup'] = pd.to_datetime(yellow_2019['tpep_pickup_datetime'],
                              infer_datetime_format=True)

yellow_2019['pickup'].head()

del yellow_2019['tpep_pickup_datetime']

yellow_2019['dropoff'] = pd.to_datetime(yellow_2019['tpep_dropoff_datetime'],
                              infer_datetime_format=True)

del yellow_2019['tpep_dropoff_datetime']

#Calculating ride duration
yellow_2019['duration'] = yellow_2019['dropoff'] - yellow_2019['pickup']


yellow_2019[['pickup','dropoff','duration']].head()


##Curating Data based on requrionments from lab 

""" # Rules we agree to
# trip_distance <= 100- (curated!)
# delete any rows where passengers = 0 (curated!) 
# delete trip distance = 0 (curated!)
# for total_amount make greater than zero but less than 1,000 (curated!)
# make "extra" >= 0"""

#Deleting rows where trip distance <=100

yellow_2019['trip_distance'].describe()

yellow_2019['valid'] = yellow_2019['trip_distance'] <= 100

yellow_2019[['trip_distance','valid']].head()

yellow_2019['trip_distance'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['trip_distance'].describe()

#Deleting rows where passenegers=0

del yellow_2019['valid']

yellow_2019['passenger_count'].describe()

yellow_2019['valid'] = yellow_2019['passenger_count'] != 0

yellow_2019[['passenger_count','valid']].head()

yellow_2019['passenger_count'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['passenger_count'].describe()

# deleting rows wehre trip distance = 0 

del yellow_2019['valid']

yellow_2019['trip_distance'].describe()

yellow_2019['valid'] = yellow_2019['trip_distance'] != 0

yellow_2019[['trip_distance','valid']].head()

yellow_2019['trip_distance'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['trip_distance'].describe()

#Deleting rows where total amount not between 0,1000:
#First I'll delete rows where total amounnt is <0

del yellow_2019['valid']

yellow_2019['total_amount'].describe()

yellow_2019['valid'] = yellow_2019['total_amount'] > 0

yellow_2019[['total_amount','valid']].head()

yellow_2019['total_amount'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['total_amount'].describe()

#Now I'll delete rows where total amount is <1000

del yellow_2019['valid']

yellow_2019['total_amount'].describe()

yellow_2019['valid'] = yellow_2019['total_amount'] < 1000

yellow_2019[['total_amount','valid']].head()

yellow_2019['total_amount'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['total_amount'].describe()

#Making Extra >=0

del yellow_2019['valid']

yellow_2019['extra'].describe()

yellow_2019['valid'] = yellow_2019['extra'] >= 0

yellow_2019[['extra','valid']].head()

yellow_2019['extra'].describe()

yellow_2019 = yellow_2019[yellow_2019.valid == True]

yellow_2019['extra'].describe()

#Summarizing variables to make sure that all conditons are met 

yellow_2019[['extra', 'trip_distance', 'passenger_count', 'total_amount']].describe()

yellow_2019.describe()
#saving means for trip distance, duration, and total_amount

#Generating summary statstics for variables of interest

yellow_2019[['total_amount','duration', 'trip_distance']].describe()

#trip distance
mean_trip_distance=yellow_2019['trip_distance'].mean()

mean_trip_distance

#duration
yellow_2019['duration'].describe()
mean_duration=yellow_2019['duration'].mean()

mean_duration

#total amount
yellow_2019['total_amount'].describe()
mean_total_amount=yellow_2019['total_amount'].mean()

mean_total_amount



count=yellow_2019['total_amount'].count()
count



"""Repeating Process for Taxi Cab 2020 Data """


yellow_2020 = pd.read_csv("yellow_tripdata_2020-06.csv")

yellow_2020
#Rounding to 5 deciimal places to make summary statistics easier to work with 
pd.set_option('display.float_format', lambda x: '%.5f' % x)

#Looking at variables 

yellow_2020.columns

#Getting to know what type of data we have

yellow_2020.dtypes

yellow_2020['tpep_pickup_datetime'].head()


#Converting pickup and dropoff times from objects to date/time format

yellow_2020['pickup'] = pd.to_datetime(yellow_2020['tpep_pickup_datetime'],
                              infer_datetime_format=True)

yellow_2020['pickup'].head()

del yellow_2020['tpep_pickup_datetime']

yellow_2020['dropoff'] = pd.to_datetime(yellow_2020['tpep_dropoff_datetime'],
                              infer_datetime_format=True)


del yellow_2020['tpep_dropoff_datetime']

#Calculating ride duration
yellow_2020['duration'] = yellow_2020['dropoff'] - yellow_2020['pickup']


yellow_2020[['pickup','dropoff','duration']].head()


##Curating Data based on requrionments from lab 

""" # Rules we agree to
# trip_distance <= 100- (curated!)
# delete any rows where passengers = 0 (curated!) 
# delete trip distance = 0 (curated!)
# for total_amount make greater than zero but less than 1,000 (curated!)
# make "extra" >= 0"""

#Deleting rows where trip distance <=100

yellow_2020['trip_distance'].describe()

yellow_2020['valid'] = yellow_2020['trip_distance'] <= 100

yellow_2020[['trip_distance','valid']].head()

yellow_2020['trip_distance'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['trip_distance'].describe()

#Deleting rows where passenegers=0

del yellow_2020['valid']

yellow_2020['passenger_count'].describe()

yellow_2020['valid'] = yellow_2020['passenger_count'] != 0

yellow_2020[['passenger_count','valid']].head()

yellow_2020['passenger_count'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['passenger_count'].describe()

# deleting rows wehre trip distance = 0 

del yellow_2020['valid']

yellow_2020['trip_distance'].describe()

yellow_2020['valid'] = yellow_2020['trip_distance'] != 0

yellow_2020[['trip_distance','valid']].head()

yellow_2020['trip_distance'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['trip_distance'].describe()

#Deleting rows where total amount not between 0,1000:
#First I'll delete rows where total amounnt is <0

del yellow_2020['valid']

yellow_2020['total_amount'].describe()

yellow_2020['valid'] = yellow_2020['total_amount'] > 0

yellow_2020[['total_amount','valid']].head()

yellow_2020['total_amount'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['total_amount'].describe()

#Now I'll delete rows where total amount is <1000

del yellow_2020['valid']

yellow_2020['total_amount'].describe()

yellow_2020['valid'] = yellow_2020['total_amount'] < 1000

yellow_2020[['total_amount','valid']].head()

yellow_2020['total_amount'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['total_amount'].describe()

#Making Extra >=0

del yellow_2020['valid']

yellow_2020['extra'].describe()

yellow_2020['valid'] = yellow_2020['extra'] >= 0

yellow_2020[['extra','valid']].head()

yellow_2020['extra'].describe()

yellow_2020 = yellow_2020[yellow_2020.valid == True]

yellow_2020['extra'].describe()

#Summarizing variables to make sure that all conditons are met 

yellow_2020[['extra', 'trip_distance', 'passenger_count', 'total_amount']].describe()

yellow_2020.describe()

#Generating summary statstics for variables of interest

yellow_2020[['total_amount','duration', 'trip_distance']].describe()

#saving means for trip distance, duration, and total_amount

#trip distance
mean_trip_distance_=yellow_2020['trip_distance'].mean()

mean_trip_distance_

#duration
yellow_2020['duration'].describe()
mean_duration_=yellow_2020['duration'].mean()

mean_duration_

#total amount
yellow_2020['total_amount'].describe()
mean_total_amount_=yellow_2020['total_amount'].mean()

mean_total_amount_



count_=yellow_2020['total_amount'].count()
count_

#Creating dictionary so that I can turn into data fram and print nicely 

#Converting count so I can use in dictionary 

count_float=float(count)
count
count_float_=float(count_)
count_float_

#Converting duration to string so I can shorten it and make table more readable
mean_duration
string_mean_duration=str(mean_duration)
string_mean_duration=string_mean_duration[7:20]
string_mean_duration


mean_duration_
string_mean_duration_=str(mean_duration_)
string_mean_duration_=string_mean_duration_[7:20]
string_mean_duration_




taxi_dict = {'Trip Distance': [(mean_trip_distance),(mean_trip_distance_)],
             'Duration':[(string_mean_duration),(string_mean_duration_)], 
             'Total Amount':[(mean_total_amount),(mean_total_amount_)],
             'Number of Records':[(count_float),(count_float_)]}
             

taxi_table = pd.DataFrame(taxi_dict)

taxi_table.index=['2019', '2020']
taxi_table

print(taxi_table)
