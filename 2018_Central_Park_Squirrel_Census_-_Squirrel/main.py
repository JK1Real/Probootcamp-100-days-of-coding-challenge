import pandas as pd


data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Making a new csv file with data of count of different suirrels with different fur color

# Listing colors of the suirrels present
color = data['Primary Fur Color'].unique().tolist()[1:]
print(color)

# Finding the number of squirrels with different fur color
count = []
count.append(len(data[data['Primary Fur Color'] == 'Gray']))
count.append(len(data[data['Primary Fur Color'] == 'Cinnamon']))
count.append(len(data[data['Primary Fur Color'] == 'Black']))


# covnerting the data into a dataframe
squirrel_data = pd.DataFrame({"Fur Color":color,"Count":count})
print(squirrel_data)

# Saving the data into a csv file
squirrel_data.to_csv("Squirrel_count.csv")