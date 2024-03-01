#Shuhena Begum
#CSC 4110

import csv
import json
import tkinter as tk
from tkinter import *
from tkinter import messagebox

#Here is the empty sales data list
sales_data = []

#Here it is opening and reading the CSV file SalesJan2009.csv.
with open('SalesJan2009.csv', 'r') as my_csvFile:
    #Here it is reading the CSV file
    read_csv = csv.reader(my_csvFile)

    #This skips a line
    next(read_csv, None)

    #Here it goes through every row in the CSV file and organizes it.
    for i in read_csv:
        #Each piece of data is being processed here
        Transaction_date = i[0]
        Product = i[1]
        Price = int(i[2])
        Payment_Type = i[3]
        
        #Here it gets rid of the extra quote characters from each piece of data.
        Name = i[4].strip('"')  
        City = i[5].strip('"')
        State = i[6].strip('"')
        Country = i[7].strip('"')

        #Here I am appending everything to the sales_data
        my_json_dict = {
            'Transaction_date': Transaction_date,
            'Product': Product,
            'Price': Price,
            'Payment_Type': Payment_Type,
            'Name': Name,
            'City': City,
            'State': State,
            'Country': Country
        }
        sales_data.append(my_json_dict)

#Here I am saving my sales data list to a file called transaction_data.json.
#Here it will write all the information from my sales data list and organize it to it's fields
with open('transaction_data.json', 'w') as json_file:
    json.dump(sales_data, json_file, indent=4)

#This is the main window that allows you to quit 
my_widget = tk.Tk()
my_widget.title("Sales Data")
my_widget.geometry("300x120")

#Here I set my UI color scheme to my old schools color
my_widget .configure(bg="blue")

#This is the UI that shows at the top level of the main window
#Here is the quit function that kills the window and process I also used messagebox to ask the user if they want to quit.
def quitp():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        #Here it says goodbye in the window once the button is clicked.
        print("goodbye!")
        #Here I used the .quit() method.
        my_widget.quit()
        #Here it will ask again if you want to kill the process and kills all window
        exit()
    
#Here is the quit button
myquit = tk.Button(my_widget, text = "QUIT", command = quitp)
myquit.pack()


#Here I utilized the message box widget in my UI to verify if user will use the program again. 
def my_message():
    mb = tk.messagebox.askquestion("verify", "Will you use this program again?")
    if mb == 'yes':
        print("YAY! Come again next time!")
    elif mb == 'no':
        print("Sorry we could not help you!")
        exit()
        
        
#Here I created a button that asks the user will they use the program again
my_ui = tk.Button(None, text="Will you use the program again?", command = my_message)
my_ui.pack()


#Here the mainloop will be running.
my_widget.mainloop()
