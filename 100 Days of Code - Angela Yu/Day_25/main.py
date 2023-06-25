# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as weather_data:
#     data = csv.reader(weather_data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
#

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)

# Get data in rows
# print(data[data.day == "Monday"])
# c = int(data[data.temp == data.temp.max()])

# Creating a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

# squirrel count
import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

GreySquirrelCount = len(data[data["Primary Fur Color"] == "Grey"])
print(GreySquirrelCount)
