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

#End of Global Functions

#Main
input = input(print("What would you like to do"))

#Main menu
#Create
if input == 1:
    print("test")
#View
elif input == 2:
    print("test")
#Update
elif input == 3:
    print("test")
#Delete
elif input == 4:
    print("test")
#Record
elif input == 5:
    print("test")
#Exit
elif input == 6:
    print("test")