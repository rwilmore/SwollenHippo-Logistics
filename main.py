#Purpose:
#Author: Ryan Wilmore
#Date: 13 October 2026

import sqlite3

#Start of Global Functions
#Create 
def addCustomer(strCustomerID,strCompanyName,strContactFirstName,strContactLastName,strEmail,strPhone,strCity,strState,strCustomerType):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        #Prepared statement
        #Question marks align with the values being inserted
        strQuery = f"INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?)"
        #'{strCustomerID}','{strCompanyName}','{strContactFirstName}','{strContactLastName}','{strEmail}','{strPhone}','{strCity}','{strState}','{strCustomerType}'
        tupValues = (strCustomerID,strCompanyName,strContactFirstName,strContactLastName,strEmail,strPhone,strCity,strState,strCustomerType)
        objCursor = conLogistics.cursor()
        #Using the tupValues
        objCursor.execute(strQuery,tupValues)

        conLogistics.commit()
    conLogistics.close()

#Read
def getCustomer(strCustomerID):
    strQuerry = ""
    if strCustomerID == "A":
        strQuery = "SELECT * FROM customers"
    else:
        strQuery = f"SELECT * FROM customers WHERE CustomerID = '{strCustomerID}'"
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstRows = objCursor.fetchall()
        print(lstRows)

    conLogistics.close()

#Update
def updateCustomer(strCustomerID,strCompanyName,strContactFirstName,strContactLastName,strEmail,strPhone,strCity,strState,strCustomerType):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        #Prepared statement
        #Question marks align with the values being inserted
        strQuery = f"UPDATE customers SET CompanyName = ?, ContactFirstName = ?, ContactLastName = ?, Email = ?, Phone = ?, City = ?, State = ?, CustomerType = ? WHERE CustomerID = ?"
        #'{strCustomerID}','{strCompanyName}','{strContactFirstName}','{strContactLastName}','{strEmail}','{strPhone}','{strCity}','{strState}','{strCustomerType}'
        tupValues = (strCompanyName,strContactFirstName,strContactLastName,strEmail,strPhone,strCity,strState,strCustomerType,strCustomerID)
        objCursor = conLogistics.cursor()
        #Using the tupValues
        objCursor.execute(strQuery,tupValues)

        conLogistics.commit()
    conLogistics.close()

#Delete
def deleteCustomer(strCustomerID):
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        #Prepared statement
        #Question marks align with the values being inserted
        strQuery = f"DELETE FROM customers WHERE CustomerID = ?"
        #'{strCustomerID}','{strCompanyName}','{strContactFirstName}','{strContactLastName}','{strEmail}','{strPhone}','{strCity}','{strState}','{strCustomerType}'
        tupValues = (strCustomerID,)
        objCursor = conLogistics.cursor()
        #Using the tupValues
        objCursor.execute(strQuery,tupValues)

        conLogistics.commit()
    conLogistics.close()

def main():

    print("-----Welcome to Swollen Hippo Logistics-----")
    print("Choose from the options below:")
    print("1. Create a new package shipment.")
    print("2. View the shipping information for an existing package (Including the tracking history of a package).")
    print("3. Update the shipping information for an existing package.")
    print("4. Delete an existing package.")
    print("5. Record the arrival of a package at a regional shipping facility.")
    print("6. Exit the application.")

    strChoice = input("What would you like to do")

    #Main menu
    #Create
    if strChoice == "1":
        print("test")
    #View
    elif strChoice == "2":
        print("test")
    #Update
    elif strChoice == "3":
        print("test")
    #Delete
    elif strChoice == "4":
        print("test")
    #Record
    elif strChoice == "5":
        print("test")
    #Exit
    elif strChoice == "6":
        print("test")

main()