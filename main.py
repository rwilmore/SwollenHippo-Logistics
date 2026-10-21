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
def getShippingInformation():
    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:

        #Gets tracking number from user
        strTrackingNumber = input("Please enter the Tracking Number of the Package you wish to view its information.")
        tupValues = (strTrackingNumber,)

        #Open database and converts the row of TrackingNumber into a list
        strQuery = "SELECT TrackingNumber FROM Packages"
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstTrackingNumbers = objCursor.fetchall()

        #Default state for blnDoesTrackingNumberExist = False so that only if it does exist
        #will the program switch it to true
        blnDoesTrackingNumberExist = False

        #Iterates through the list to find the correct number if available
        for objTrackingNumber in lstTrackingNumbers:
        
            #Note: I used AI to understand an issue and fix this line of code vvv
            #Figured out that an entire tuple could not be compared to a string
            #So it was always returning false
            if objTrackingNumber[0] == strTrackingNumber:
        
                #If there blnDoesTrackingNumberExist returns true
                blnDoesTrackingNumberExist = True

         #Using the value of blnDoesTrackingNumberExist 
        if blnDoesTrackingNumberExist == True:

            strQuery = f"SELECT * FROM Packages WHERE TrackingNumber = ?"
            objCursor = conLogistics.cursor()
            objCursor.execute(strQuery,tupValues)
            lstRows = objCursor.fetchall()
            
            print("\n-----PACKAGE SHIPPING INFORMATION-----")
            print(f"Tracking Number: {lstRows[0][0]}")
            print(f"First Name: {lstRows[0][1]}")
            print(f"Last Name: {lstRows[0][2]}")
            print(f"Destination Company: {lstRows[0][3]}")
            print(f"Destination Street Address: {lstRows[0][4]}")
            print(f"Destination City: {lstRows[0][5]}")
            print(f"Destination State: {lstRows[0][6]}")
            print(f"Destination ZIP Code: {lstRows[0][7]}")
            print(f"Originating Customer: {lstRows[0][8]}")
            print(f"Originating Facility: {lstRows[0][9]}")
            print("--------------------------------------\n")

        else:
            print("\nThere was no package with that tracking number. Please try again.\n")

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

        #Gets tracking number from user
        strTrackingNumber = input("What is the Tracking Number of the Package you wish to Delete? : ")

        #Open database and converts the row of TrackingNumber into a list
        strQuery = "SELECT TrackingNumber FROM Packages"
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstTrackingNumbers = objCursor.fetchall()

        #Default state for blnDoesTrackingNumberExist = False so that only if it does exist
        #will the program switch it to true
        blnDoesTrackingNumberExist = False

        #Iterates through the list to find the correct number if available
        for objTrackingNumber in lstTrackingNumbers:

            #Note: I used AI to understand an issue and fix this line of code vvv
            #Figured out that an entire tuple could not be compared to a string
            #So it was always returning false
            if objTrackingNumber[0] == strTrackingNumber:

                #If there blnDoesTrackingNumberExist returns true
                blnDoesTrackingNumberExist = True

        #Using the value of blnDoesTrackingNumberExist 
        if blnDoesTrackingNumberExist == True:

            #Opens the database and uses the tracking number to find the row
            #associated with it and print off all of the information
            strQuery = f"SELECT * FROM Packages WHERE TrackingNumber = '{strTrackingNumber}'"
            objCursor = conLogistics.cursor()
            objCursor.execute(strQuery)
            lstRows = objCursor.fetchall()
            print(lstRows)

            #Ask the user if this is the correct package they wish to delete
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

        elif blnDoesTrackingNumberExist == False:
            print("There was no package with that tracking number. Please try again.")
    conLogistics.close()

#Record
def recordArrivalOfPackage():
    print("This is a placeholder")

def mainMenu():

    print("----------------------------------------Swollen-Hippo-Logistics----------------------------------------")
    print("1. Create a new package shipment.")
    print("2. View the shipping information for an existing package (Including the tracking history of a package).")
    print("3. Update the shipping information for an existing package.")
    print("4. Delete an existing package.")
    print("5. Record the arrival of a package at a regional shipping facility.")
    print("6. Exit the application.")
    print("-------------------------------------------------------------------------------------------------------")

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

