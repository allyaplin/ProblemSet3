#-------------------------------------------------------------
# ProblemSet3_Part1.py
#
#Description: Problem Set 3 for Writing Scripts practice in VS Code
# Author: Ally Aplin (allison.aplin@duke.edu)
# Date:   Fall 2024
#----------
#%% Task 1 - Edit code to print as requested
# Variables
mountain = "Denali"
nickname = '"Mt. McKinley"' #add quotes around name
elevation = 20322  # Corrected the assignment operator == to =

# Minimal edits to achieve correct output
print(mountain + ", formerly\nknown as " + nickname)  # Use \n for new lines and change quotes for nickname
print("is " + str(elevation) + "' feet above sea level.")  # Add str() to convert elevation to a string and add ' after

#%% Task 2 - Lists and Iteration
# Step 1: Assign the data_folder string to  “W:\859_data\triangle"
data_folder = "W:\\859_data\\triangle" #double \\ so it doesn't think i mean escape character

# Step 2: Create a list called data_list with string objects
data_list = ["streams.shp", "stream_types.csv", "naip_imagery.tif"]

# Step 3: Assign the variable user_item to "roads.shp" string
user_item = "roads.shp"

# Step 4: Add user_item to the data_list list you already have made with append.
data_list.append(user_item)

# Step 5: Loop through each item in data_list and print the window path for each dataset
for item in data_list:
    full_path = data_folder + "\\" + item  # Concatenate folder path and file name
    print(full_path)

# %% Task 3 - Lists and iteration

