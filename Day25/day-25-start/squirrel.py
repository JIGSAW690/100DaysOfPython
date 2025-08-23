import pandas

squirrel_data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250810.csv')
#squirrel_list = squirrel_data['Primary Fur Color'].tolist()

red = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon'])
grey = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray'])
black = len(squirrel_data[squirrel_data['Primary Fur Color'] == 'Black'])

"""
for squirrel in squirrel_list:
    if str(squirrel).lower() == 'cinnamon':
        red += 1
    elif str(squirrel).lower() == 'gray':
        grey += 1
    elif str(squirrel).lower() == 'black':
        black += 1
"""

squirrel_dict = {
    'Fur Color': ['Gray', 'Red', 'Black'],
    'Count': [grey, red, black]
}

new_data = pandas.DataFrame(squirrel_dict)
new_data.to_csv('squirrel_data.csv')
