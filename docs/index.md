# The Pickled Exception

Kristen Burke

August 24, 2021

IT FDN 110A

Assignment 07



## Introduction
This assignment asked for a program that would demonstrate pickling and error handling. This project was somewhat open-ended, with no starting material provided and instructions to do more research. The assignment was coded in PyCharm. 

## Functions and Concepts Used
Pickling is when data is stored into a binary file instead of a text file. This allows for larger chunks of data to be stored in a smaller space. When a file is unpickled, the data will be reverted back to its usual form. The main functions used for pickling are dump() and load(), respectively for putting data into the file and loading it back out. 

This module also explored error handling in python. Sometimes, a user inputs some bad data and causes the script to stop and throw a confusing error message. Or a file read by the program has no data left and stops the program instead of just moving to the next step. Using a try-except block of code can help get around these situations and keep the program running. Python has standard exceptions but custom ones can also be created. 

## Creating and Editing the Program
Since this program had to be created from scratch, I decided to keep it as simple as possible to demonstrate the key concepts accurately. I pulled from my work on the previous project to create a simple program that asks the user for some data, pickles that data, and then unpickles it into a list. 
As usual, I started with a header and defining some variables (Figure 1).
```
# ------------------------------------------------- #
# Title: Assignment 07
# Description: An example of how pickling and error handling works
# ChangeLog: (Who, When, What)
# KBurke,8/24/2021,Created Script
# ------------------------------------------------- #

# variables defined ------------

strFileName = "PickleData.dat"
lstFlower = [] # list of data to be gathered from user and pickled
strChoice = "" # menu choice inputted from user
```

Next, I defined my functions for pickling and unpickling the data (Figure 2). Here is also where I realized I would need to use a try-except block. The load function only pulls one row of data from the binary file so it would need to be run over and over again. But eventually, the file will run out of data to unpickle and throw an end-of-file error. An exception here allows the script to keep moving with whatever it did pull from the file. 
```
# processing -------------------
import pickle

def save_data_to_file(file_name, list_of_data):
    objFile = open(file_name, "ab") # opens file
    pickle.dump(list_of_data, objFile) # writes data to binary file
    objFile.close()

def read_data_from_file(file_name):
    list_of_data = []
    with open(file_name, "rb") as objFile:
        while True:
            try: # error handling block
                data = pickle.load(objFile) # loads row of data from file
                list_of_data.append(data) # appends to list
            except EOFError: # stops end of file error condition
                break
    objFile.close()
    return list_of_data
```

I also defined some simple presentation functions (Figure 3). 
```

def print_menu():
   # Display a menu of choices to the user
    print('''
    Menu of Options
    1) Add a new flower to list
    2) Save data to file 
    3) Display all data from file  
    4) Exit   ''')
    print()  # Add an extra line for looks

def input_menu_choice():
    # Gets the menu choice from a user
    choice = input("Which option would you like to perform? [1 to 4] - ").strip()
    print()  # Add an extra line for looks
    return choice

def input_user_data():
    strData = input("Enter a type of flower:  ")  # input prompt
    lstFlower = [strData]
    return lstFlower
```

Finally, I constructed the main part of the script, calling the functions under their designated menu options (Figure 4). 
```
while (True):
    print('''This program asks for user flower preference and 
      stores the data in a binary file.''') # printed instructions and info
    print_menu()
    strChoice = input_menu_choice()

    if strChoice == "1":
        lstFlower = input_user_data()
        continue

    elif strChoice == "2":
        save_data_to_file(strFileName, lstFlower)  # call save data function
        print("Flower data saved!")
        print()
        continue

    elif strChoice == "3":
        print("Data in file:")
        print(read_data_from_file(strFileName))
        continue

    elif strChoice == "4":
        print("Goodbye!")
        break  # and Exit program
```

## Running the Program
I first ran through the program in PyCharm, verifying that each option does what it is supposed to do (Figure 5). 
![Figure 5a](/docs/Fig5aresize.png "Figure 5a")![Figure 5b](/docs/Fig5bresize.png "Figure 5b")
![Figure 5c](/docs/Fig5cresize.png "Figure 5c")![Figure 5d](/docs/Fig5dresize.png "Figure 5d")

The script was also tested from the command window (Figure 6). 
![Figure 6](/docs/Fig6resize.png "Figure 6")


## Conclusion
While the script could definitely be more polished, I think it demonstrates an example of how to use the concepts in the module. In the future, I would probably find a way to organize the pickled data so that it is more readable when it is unpickled. 


