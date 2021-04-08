import csv
import datetime
#run pip install tabulate in python terminal
from tabulate import tabulate


def get_name():
    print('Enter the name of the medicine')
    Name=input()
    return Name

    pass
def ID(Name):
    import random
    ID = Name[0:2] + str(random.randint(1, 4))
    return ID
    pass
def get_Price_in_QAR():
    try:
        Price=float(input('Enter medicine price in qatari ryals'))
        while Price < 0.5:
            print('invalid value, should be greater than or equal to 0.5')
            Price=float(input('please enter a valid price'))
        return Price    
    except ValueError:
        print('invalid value, the value should be written in numbers')   
    pass
def get_type():
    print('enter the category of the medicine')
    print('1 for Prescription Only Medicines (POM), 2 for Pharmacy Medicines (P), or 3 for General sales list (GSL)')
    Type = int(input('please enter 1, 2 or 3'))
    while Type != 1 and Type != 2 and Type != 3:
        print('invalid medicine type')
        Type = int(input('enter a valid medicine type'))
    return Type
    pass
def get_quantity():
    try:
        Quantity=int(input('Enter medicine quantity'))
        while Quantity < 0:
            print('invalid value, quantity cannot be a negative number')
            Quantity=int(input('please enter a valid value fo medicine quantity'))
        return Quantity
    except ValueError:
        print('invalid value, quantity should be written in numbers not letters')

    pass

def get_Quantity_sold():
    try:
        Quantity_sold = int(input('Enter the sold quantity of the medicine'))
        while Quantity_sold < 0:
            print('invalid value, sold quantity cannot be a negative number')
            Quantity_sold = int(input('please enter a valid value for the sold quantity of the medicine'))
        return Quantity_sold
    except ValueError:
        print('invalid value, sold quantity should be written as a whole number not in letters')
    pass
def get_Exp_date():
    print("Enter the expiry date for the medicine (dd/mm/yyyy)")
    exDate = input()
    exDate = str(datetime.datetime.strptime(exDate, "%d/%m/%Y").date())
    return exDate
    pass


def showExpiryDate():
    exDateList = []
    currentDate = datetime.datetime.today().date()
    with open("pharmacy.txt", 'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            Date = datetime.datetime.strptime(row[6], "%Y-%m-%d").date()
            if (currentDate.year == Date.year) and (currentDate.month - Date.month) < 3:
                exDateList.append(row)
        if not exDateList:
            print("No medicines expire within 3 months")
        else:
            print(tabulate(exDateList,
                           headers=["Type", "ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date",
                                    "Available Stock"], tablefmt='psql'))
    pass


def showStock10():
    stockItemList = []
    with open("pharmacy.txt", 'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            if int(row[7]) < 10:
                stockItemList.append(row)
    if not stockItemList:
        print("Items with stock less than 10: None")
    else:
        print(tabulate(stockItemList,
                       headers=["Type", "ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date",
                                "Available Stock"], tablefmt='psql'))
    pass
def updateInventory(Med_ID):
    # TIP: keep this data visualization in mind
    # the next line shows a list of lists, for this program, each list inside the list is referred to as a row THUS:
    # [[2,PA1,Panadol,11.0,15,32,27102021],[1,AU3,Augmenting,34.0,167,98,01092021]]
    # (1,AU3,Augmenting,34.0,167,98,01092021) is a row and each element has an index, so row[0] corresponds to Type,.etc

    with open('pharmacy.txt') as csvFile:
        # opens pharmacy.txt for read, and runs the segment if it was opened successfully
        dataSelect = csv.reader(csvFile, delimiter=',') # dataSelect holds csv file data, in an array like type
        List = list(dataSelect) # force change data type into a list (results in a list of lists aka 2D array)
        for row in List: # looping through each dimention
            if row[1] == Med_ID: # if Med ID is found
                # print relevant data for user confirmation
                print(f" Type : {row[0]}\n ID : {row[1]}\n Name :{row[2]}\n Price : {row[3]}\n quantity : {row[4]}\n quantity sold :{row[5]}\n Expiry Date : {row[6]} ")
                print("Which value you are willing to edit?  (Select a number)")
                print("1. quantity")
                print("2. Expiry Date")
                choice = input()
                if choice == "1":
                    print("Enter New quantiry")
                    NewQuantity = input()
                    row[4] = NewQuantity # updates quantity value in the list
                    writeObject = csv.writer(open("pharmacy.txt","w", newline='')) # opens pharmacy.txt as write file
                    writeObject.writerows(List) # writes the Updated List into pharmacy.txt file
                if choice == "2":
                    print("Enter New Date without any separators")
                    NewDate = input()
                    row[6] = NewDate
                    writeObject = csv.writer(open("pharmacy.txt", "w", newline=''))
                    writeObject.writerows(List)
        csvFile.close()


    pass

# search and delete function definition
def searchAndDelete(medID, medType):
    # following the same method in UpdateInventory function
    with open("pharmacy.txt") as csvFile:
        dataMed = csv.reader(csvFile, delimiter=',')
        List = list(dataMed)
        for row in List:
            if row[0] == medType and row[1] == medID: # find a row which has bot Type & ID values equal to user input
                print("MED found")
                print(f" Type : {row[0]}\n ID : {row[1]}\n Name :{row[2]}\n Price : {row[3]}\n quantity : {row[4]}\n quantity sold :{row[5]}\n Expiry Date : {row[6]} ")
                print("are you sure you want to delete the data above? (y/n)")
                answer = input()
                if answer == 'y' or answer == 'Y':
                    rowIndex = List.index(row)
                    List.pop(rowIndex)
                    writeObject = csv.writer(open("pharmacy.txt", "w", newline=''))
                    writeObject.writerows(List)
                else: pass

    pass


def billing():
    print("Choose the Medicine")
    with open("pharmacy.txt") as csvFile:
        dataMed = csv.reader(csvFile, delimiter=',')
        List = list(dataMed)
        for row in List: # a loop through all the list printing ID,Price,quantity available of all products
            print(f" ID : {row[1]}  Price : {row[3]}  Quantity available : {row[4]}")
        for row in List: # Billing loop
            print("MED ID: ")
            medID = input()
            if medID == row[1]: # find med id entered by the user in the list
                print("type the Amount you want to buy:")
                medAmount = input() # get the amount the user is willing to buy
                AmountBuy = int(medAmount) # force user input to integer type
                AmountSell =  int(row[4])  # get amount available
                if AmountBuy <= AmountSell: # if amount desired by the user less than or equal stock proceed
                    print("Your Bill")
                    print(f"Medicine Name : {row[2]} \nQuantity purchased : {AmountBuy}\nPrice : {AmountBuy*float(row[3])}")
                    AmountSell -= AmountBuy # subtracts user input from amount available
                    row[4] = str(int(row[4])-AmountBuy) # updates quantity available of the med
                    row[5] = str(int(row[5])+AmountBuy) # updates quantity sold of the med
                    writeObject = csv.writer(open("pharmacy.txt", "w", newline=''))
                    writeObject.writerows(List)
                    break
                else:
                    print("amount desired exceeds out stock")
                    print("submit new request \n")
                    continue
            else:
                print("Medicine Not Available")
                pass
    pass


def histoGramDisplay():
    # remember to use "pip install matplotlib"
    # Tip: Listprice here hold a 2D list serving as the DataBase or Frequency counter.
    # this segment will create price list similar to this:
    # [name1,name1,name1,name1,name1,name1
    # name2,name2,name2,name2,name2,name2]

    import matplotlib.pyplot as plt
    ListPrice = [] # initializing empty list which will hold amount sold
    ListName = [] # empty list which will hold med names
    with open('pharmacy.txt')as csvFile:
        read = csv.reader(csvFile, delimiter=',')
        for row in read: # executing this loop for each row separately
            i=0 # loop control
            range = int(row[5]) # histogram max data range
            while i<range:
                i+=1
                ListPrice.append(row[2]) # appends med name to the price list once each iteration till range is reached
            ListName.append(row[2]) # append med name to Name list
        plt.hist(ListPrice, bins=ListName, ) # plots the histogram
        plt.show() # shows the histogram
    pass

while True:
    print("welcome to the pharmacy application")
    print("please choose the operation type (by letter")
    print("A. Add a new medicine")
    print("B. show the inventory")
    print("C. Update the inventory")
    print("D. search and delete")
    print("E. billing")
    print("F. plot Histogram")
    print("G. exit application")
    choice = input()
    if choice == "A" or choice == "a":
        print('Enter the following new medicne data:')
        Type = get_type()
        Med_Name = get_name()
        Med_ID = ID(Med_Name)
        Price = get_Price_in_QAR()
        Quantity = get_quantity()
        Quantity_sold = get_Quantity_sold()
        Exp_date = get_Exp_date()
        available_stock = Quantity - Quantity_sold
        list = [Type, Med_ID, Med_Name, Price, Quantity, Quantity_sold, Exp_date, available_stock]
        with open("pharmacy.txt", 'a') as csvFile:
            write_file = csv.writer(csvFile)
            write_file.writerow(list)
            csvFile.close()
    if choice == "b" or choice == "B":
        with open("pharmacy.txt", 'r') as csvFile:
            readFile = csv.reader(csvFile)
            print(tabulate(readFile, headers=["Type", "ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date",
                                              "Available Stock"], tablefmt='psql'))
        csvFile.close()
        print("if you want to view items with expiry date of three months press e/E")
        print("if you want to view items with available stock less than 10 press l/L")
        choice2 = input()
        if choice2 == "e" or choice2 == "E":
            showExpiryDate()
        if choice2 == "l" or choice2 == "L":
            showStock10()
    elif choice == "c" or choice == "C":  # choice# 3
        print("please type the MED ID you desire to edit")
        Med_ID = input()
        updateInventory(Med_ID)  # update inventory function with Med ID as parameter
    elif choice == "d" or choice == "D":  # choice# 4
        print("Please Type in the TYPE number")
        medType = input()
        print("Please enter the ID of a medicine")
        medID = input()
        searchAndDelete(medID, medType)
    elif choice == "e" or choice == "E":  # choice# 5
        billing()
    elif choice == "f" or choice == "F":  # choice# 6
        histoGramDisplay()
    if choice == "g" or choice == "G":
        break

