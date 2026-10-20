#Purpose:
#Author: Ryan Wilmore
#Date: 13 October 2026

import sqlite3

#Start of Global Functions
#Create 
def addPackageShipment():
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        #Prepared statement
        #Question marks align with the values being inserted
        strQuery = f"INSERT INTO Packages VALUES (?,?,?,?,?,?,?,?,?,?)"

        strTrackingNumber = input("Enter the Tracking Number: ")
        if strTrackingNumber == "":
            print("Error. Tracking Number cannot be blank! Please try again.")
            strTrackingNumber = input("Enter the Tracking Number: ")

        strDestinationFirstName = input("Enter the Destination First Name: ")
        if strDestinationFirstName == "":
            print("Error. Destination First Name cannot be blank! Please try again.")
            strDestinationFirstName = input("Enter the Destination First Name: ")

        strDestinationLastName = input("Enter the Destination Last Name: ")
        if strDestinationLastName == "":
            print("Error. Destination Last Name cannot be blank! Please try again.")
            strDestinationLastName = input("Enter the Destination Last Name: ")

        strDestinationCompany = input("Enter the Destination Company: ")
        if strDestinationCompany == "":
            print("Error. Destination Company cannot be blank! Please try again.")
            strDestinationCompany = input("Enter the Destination Company: ")

        strDestinationStreet = input("Enter the Destination Street: ")
        if strDestinationStreet == "":
            print("Error. Destination Street cannot be blank! Please try again.")
            strDestinationStreet = input("Enter the Destination Street: ")

        strDestinationCity = input("Enter the Destination City: ")
        if strDestinationCity == "":
            print("Error. Destination City cannot be blank! Please try again.")
            strDestinationCity = input("Enter the Destination City: ")

        strDestinationState = input("Enter the Destination State: ")
        if strDestinationState == "":
            print("Error. Destination State cannot be blank! Please try again.")
            strDestinationState = input("Enter the Destination State: ")

        strDestinationZipCode = input("Enter the Destination ZIP Code: ")
        if strDestinationZipCode == "":
            print("Error. Destination ZIP Code cannot be blank! Please try again.")
            strDestinationZipCode = input("Enter the Destination ZIP Code: ")

        strOriginatingCustomer = input("Enter the Originating Customer: ")
        if strOriginatingCustomer == "":
            print("Error. Originating Customer cannot be blank! Please try again.")
            strOriginatingCustomer = input("Enter the Originating Customer: ")

        strOriginatingFacility = input("Enter the Originating Facility: ")
        if strOriginatingFacility == "":
            print("Error. Originating Facility cannot be blank! Please try again.")
            strOriginatingFacility = input("Enter the Destination Last Name: ")

        tupValues = (strTrackingNumber,strDestinationFirstName,strDestinationLastName,strDestinationCompany,strDestinationStreet,strDestinationCity,strDestinationState,strDestinationZipCode,strOriginatingCustomer,strOriginatingFacility)
        objCursor = conLogistics.cursor()
        #Using the tupValues
        objCursor.execute(strQuery,tupValues)

        conLogistics.commit()
    conLogistics.close()
    print(f"\nYour package has been recorded. Tracking number: {strTrackingNumber}\n")

#Read
def getShippingInformation(strCustomerID):
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
def updateShippingInformation(strCustomerID,strCompanyName,strContactFirstName,strContactLastName,strEmail,strPhone,strCity,strState,strCustomerType):
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
def deleteExisitingPackage():
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:

        strTrackingNumber = input("What is the Tracking Number of the Package you wish to Delete? : ")

        strQuery = f"SELECT * FROM Packages WHERE TrackingNumber = '{strTrackingNumber}'"
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstRows = objCursor.fetchall()
        print(lstRows)

        strChoice = input("Is this the Package you wish to Delete? (Y/N): ")

        if strChoice == "y" or strChoice == "Y":
            #Prepared statement
            #Question marks align with the values being inserted
            strQuery = f"DELETE FROM Packages WHERE TrackingNumber = ?"

            tupValues = (strTrackingNumber,)
            objCursor = conLogistics.cursor()
            #Using the tupValues
            objCursor.execute(strQuery,tupValues)
            
            conLogistics.commit()
        else:
            print("No Package was Deleted.")
    conLogistics.close()

#Record
def recordArrivalOfPackage():
    print("This is a placeholder")

def mainMenu():

    print("-----Welcome to Swollen Hippo Logistics-----")
    print("Choose from the options below:")
    print("1. Create a new package shipment.")
    print("2. View the shipping information for an existing package (Including the tracking history of a package).")
    print("3. Update the shipping information for an existing package.")
    print("4. Delete an existing package.")
    print("5. Record the arrival of a package at a regional shipping facility.")
    print("6. Exit the application.")

    strChoice = input("\n")

    #Main menu
    #Create
    if strChoice == "1":
        addPackageShipment()
        mainMenu()
    #View
    elif strChoice == "2":
        getShippingInformation()
        mainMenu()
    #Update
    elif strChoice == "3":
        updateShippingInformation()
        mainMenu()
    #Delete
    elif strChoice == "4":
        deleteExisitingPackage()
        mainMenu()
    #Record
    elif strChoice == "5":
        print("test")
        mainMenu()
    #Exit
    elif strChoice == "6":
        print("Exiting the application. Have a nice day!")

#End of Global Functions

#Calls the main menu
mainMenu()