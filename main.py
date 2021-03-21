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

print("welcome to the pharmacy application")
print("please choose the operation type (by letter")
print("A. Add a new medicine")
print("B. show the inventory")
print("C. Update the inventory")
print("D. search and delete")
print("E. billing")
choice = input()
if choice =="A" or choice == "a":
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


def showExpiryDate():
    exDateList = []
    currentDate = datetime.datetime.today().date()
    with open("pharmacy.txt",'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            Date = datetime.datetime.strptime(row[6], "%Y-%m-%d").date()
            if (currentDate.year == Date.year) and (currentDate.month - Date.month)<3:
                exDateList.append(row)
        if not exDateList:
            print("No medicines expire within 3 months")
        else:
            print(tabulate(exDateList, headers=["Type","ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date", "Available Stock"], tablefmt='psql'))
    pass

def showStock10():
    stockItemList = []
    with open("pharmacy.txt",'r') as csvFile:
        readFile = csv.reader(csvFile)
        for row in readFile:
            if int(row[7])<10:
                stockItemList.append(row)
    if not stockItemList:
        print("Items with stock less than 10: None")
    else: print(tabulate(stockItemList, headers=["Type","ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date", "Available Stock"], tablefmt='psql'))
    pass


if choice == "b" or choice == "B":
    with open("pharmacy.txt", 'r') as csvFile:
        readFile = csv.reader(csvFile)
        print(tabulate(readFile, headers=["Type","ID", "Name", "Price", "Quantity", "Quantity Sold", "Expiry Date", "Available Stock"], tablefmt='psql'))
    csvFile.close()
    print("if you want to view items with expiry date of three months press e/E")
    print("if you want to view items with available stock less than 10 press l/L")
    choice2 = input()
    if choice2 == "e" or choice2 == "E":
        showExpiryDate()
    if choice2 == "l" or choice2 == "L":
        showStock10()
