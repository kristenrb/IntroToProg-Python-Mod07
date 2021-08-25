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


# presentation ------------------- #

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

# main body --------------------- #

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

