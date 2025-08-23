"""
import csv

data = []
with open('weather_data.csv', 'r') as file:
   data_reader = csv.reader(file)
   data_reader.__next__()
   temparatures = []
   for row in data_reader:
       temparatures.append(int(row[1]))
for temp in temparatures:
    print(temp)
"""

import pandas
data = pandas.read_csv('weather_data.csv')
print(data['temp'])

"""
temp_list = data['temp'].tolist()
avg_temp = sum(temp_list) / len(temp_list)
print(f'Average Temparature: {avg_temp}')
"""

# mean() method of Series in Pandas will calculate the average of the series
print(f'Average Temparature : {data['temp'].mean()} degrees')

# max() method of Series in Pandas will calculate the maximum of the series
print(f'Maximum Temparature : {data['temp'].max()} degrees')

# min() method of Series in Pandas will calculate the minimum of the series
print(f'Minimum Temparature : {data['temp'].min()} degrees')

# Printing the row which has highest temparature
print(data[data.temp == data['temp'].max()])

#Printing Monday's temparature in Fahrenheit
monday = data[data.day == 'Monday']
print(f'Monday Temp in Fahrenheit: {monday['temp'] * 9/5 + 32} degrees')

#Creating a data frame from scratch and putting that data in csv format
dict = {
    'students': ['Amy', 'Bob', 'Charles', 'David'],
    'scores': [50, 60, 70, 80]
}
data_dict = pandas.DataFrame(dict)
data_dict.to_csv('Students.csv')

