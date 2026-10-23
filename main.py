#Purpose: This is a Python and SQLite tracking and managament system for SwollenHippo Logistics
#Author: Ryan Wilmore
#Date: 13 October 2026

import sqlite3

from datetime import datetime, timezone

#Converts format to XXXX-XX-XXTXX:XX:XX.XXXZ
strCurrentTime = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:00.000')+ "Z"

#Start of Global Functions
#Create 
def addPackageShipment():

    #Default values for these variables, if there are no errors, these will not be used
    blnError = False
    strError = ""

    strTrackingNumber = input("Enter the Tracking Number: ")
    if strTrackingNumber == "":
        strError += "Tracking Number cannot be blank. "
        blnError = True

    strDestinationFirstName = input("Enter the Destination First Name: ")
    if strDestinationFirstName == "":
        strError += "Destination First Name cannot be blank. "
        blnError = True

    strDestinationLastName = input("Enter the Destination Last Name: ")
    if strDestinationLastName == "":
        strError += "Destination Last Name cannot be blank. "
        blnError = True

    strDestinationCompany = input("Enter the Destination Company: ")
    if strDestinationCompany == "":
        strError += "Destination Company cannot be blank. "
        blnError = True

    strDestinationStreet = input("Enter the Destination Street: ")
    if strDestinationStreet == "":
        strError += "Destination Street cannot be blank. "
        blnError = True

    strDestinationCity = input("Enter the Destination City: ")
    if strDestinationCity == "":
        strError += "Destination City cannot be blank. "
        blnError = True

    strDestinationState = input("Enter the Destination State: ")
    if strDestinationState == "":
        strError += "Destination State cannot be blank. "
        blnError = True

    strDestinationZipCode = input("Enter the Destination ZIP Code: ")
    if strDestinationZipCode == "":
        strError += "Destination ZIP Code cannot be blank. "
        blnError = True

    strOriginatingCustomer = input("Enter the Originating Customer: ")
    if strOriginatingCustomer == "":
        strError += "Originating Customer cannot be blank. "
        blnError = True

    strOriginatingFacility = input("Enter the Originating Facility: ")
    if strOriginatingFacility == "":
        strError += "Originating Facility cannot be blank. "
        blnError = True

    if blnError == False:
        with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        
            #Prepared statement
            #Question marks align with the values being inserted
            strQuery = f"INSERT INTO Packages VALUES (?,?,?,?,?,?,?,?,?,?)"

            #Adds inputs into a tuple
            tupValues = (strTrackingNumber,strDestinationFirstName,strDestinationLastName,strDestinationCompany,strDestinationStreet,strDestinationCity,strDestinationState,strDestinationZipCode,strOriginatingCustomer,strOriginatingFacility)
            objCursor = conLogistics.cursor()

            #Using the tupValues
            objCursor.execute(strQuery,tupValues)
    
            #Creates first tracking record
            strQuery = f"INSERT INTO TrackingHistory VALUES ((SELECT MAX(TrackingID) + 1 FROM TrackingHistory),?,?,?)"
    
            tupValues = (strTrackingNumber,strOriginatingFacility,strCurrentTime)
            objCursor = conLogistics.cursor()
            #Using the tupValues
            objCursor.execute(strQuery,tupValues)
            conLogistics.commit()
        conLogistics.close()
        print(f"\nYour package has been recorded. Tracking number: {strTrackingNumber}\n")
    else:
        #Error Statement
        print(f"Error: {strError}Please try again.")
        strContinue = input("Press enter to continue.")

#Read
def getShippingInformation():

    #Gets tracking number from user
    strTrackingNumber = input("Please enter the Tracking Number of the Package you wish to view its information: ")

    #Default state for blnDoesTrackingNumberExist = False so that only if it does exist
    #will the program switch it to true
    blnDoesTrackingNumberExist = False


    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:

        #Open database and converts the row of TrackingNumber into a list
        strQuery = "SELECT TrackingNumber FROM Packages"
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstTrackingNumbers = objCursor.fetchall()

        #Iterates through the list to find the correct number if available
        for objTrackingNumber in lstTrackingNumbers:
        
            
            if objTrackingNumber[0] == strTrackingNumber:
        
                #If there blnDoesTrackingNumberExist returns true
                blnDoesTrackingNumberExist = True

         #Using the value of blnDoesTrackingNumberExist 
        if blnDoesTrackingNumberExist == True:

            tupValues = (strTrackingNumber,)
            
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

            #Tracking History
            strQuery = f"SELECT * FROM TrackingHistory WHERE TrackingNumber = ?"
            objCursor = conLogistics.cursor()
            objCursor.execute(strQuery,tupValues)
            lstRows = objCursor.fetchall()
            
            print("\n-----------Tracking-History-----------")

            #Tracking History for loop
            for row in lstRows:
                if row[2] == "TN01":
                    print("Facility: Cookeville, TN")
                elif row[2] == "NJ02":
                    print("Facility: Jersey City, NJ")
                elif row[2] == "KS01":
                    print("Facility: Kansas City, KS")                    
                elif row[2] == "CA04":
                    print("Facility: Los Angeles, CA")
                elif row[2] == "ID01":
                    print("Facility: Sioux City, ID")
                
                print(f"Time of Arrival: {row[3]}\n")

            #Current Location
            if lstRows[len(lstRows)-1][2] == "TN01":
                print("Current Location: Cookeville, TN")
            elif lstRows[len(lstRows)-1][2] == "KJ02":
                print("Current Location: Jersey City, NJ")
            elif lstRows[len(lstRows)-1][2] == "KS01":
                print("Current Location: Kansas City, KS")
            elif lstRows[len(lstRows)-1][2] == "CA04":
                print("Current Location: Los Angeles, CA")
            elif lstRows[len(lstRows)-1][2] == "ID01":
                print("Current Location: Sioux City, ID")
            print("--------------------------------------\n")

        else:
            print("\nThere was no package with that tracking number. Please try again.\n")
            strContinue = input("Press enter continue.")
    conLogistics.close()

#Update
def updateShippingInformation():

    #Default values for these variables, if there are no errors, these will not be used
    blnError = False
    strError = ""

    strTrackingNumber = input("Enter the Tracking Number: ")
    if strTrackingNumber == "":
        strError += "Tracking Number cannot be blank. "
        blnError = True

    strDestinationFirstName = input("Enter the Destination First Name: ")
    if strDestinationFirstName == "":
        strError += "Destination First Name cannot be blank. "
        blnError = True

    strDestinationLastName = input("Enter the Destination Last Name: ")
    if strDestinationLastName == "":
        strError += "Destination Last Name cannot be blank. "
        blnError = True

    strDestinationCompany = input("Enter the Destination Company: ")
    if strDestinationCompany == "":
        strError += "Destination Company cannot be blank. "
        blnError = True

    strDestinationStreet = input("Enter the Destination Street: ")
    if strDestinationStreet == "":
        strError += "Destination Street cannot be blank. "
        blnError = True

    strDestinationCity = input("Enter the Destination City: ")
    if strDestinationCity == "":
        strError += "Destination City cannot be blank. "
        blnError = True

    strDestinationState = input("Enter the Destination State: ")
    if strDestinationState == "":
        strError += "Destination State cannot be blank. "
        blnError = True

    strDestinationZipCode = input("Enter the Destination ZIP Code: ")
    if strDestinationZipCode == "":
        strError += "Destination ZIP Code cannot be blank. "
        blnError = True

    strOriginatingCustomer = input("Enter the Originating Customer: ")
    if strOriginatingCustomer == "":
        strError += "Originating Customer cannot be blank. "
        blnError = True

    strOriginatingFacility = input("Enter the Originating Facility: ")
    if strOriginatingFacility == "":
        strError += "Originating Facility cannot be blank. "
        blnError = True

    #Checks for errors
    if blnError == False:
        with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
        
            #Prepared statement
            #Question marks align with the values being inserted
            strQuery = f"UPDATE Packages SET DestinationFirstName = ?, DestinationLastName = ?, DestinationCompany = ?, DestinationStreetAddress = ?, DestinationCity = ?, DestinationState = ?, DestinationZIPCode = ?, OriginatingCustomer = ?, OriginatingFacilityID = ? WHERE TrackingNumber = ?"
            tupValues = (strDestinationFirstName,strDestinationLastName,strDestinationCompany,strDestinationStreet,strDestinationCity,strDestinationState,strDestinationZipCode,strOriginatingCustomer,strOriginatingFacility,strTrackingNumber)
            objCursor = conLogistics.cursor()
            #Using the tupValues
            objCursor.execute(strQuery,tupValues)

            conLogistics.commit()
        conLogistics.close()
        print(f"\nYour package has been recorded. Tracking number: {strTrackingNumber}\n")
        strContinue = input("Press enter to continue.")
    else:
        #Error Statement
        print(f"Error: {strError}Please try again.")
        strContinue = input("Press enter to continue.")

#Delete
def deleteExisitingPackage():

    #Default state for blnDoesTrackingNumberExist = False so that only if it does exist
    #will the program switch it to true
    blnDoesTrackingNumberExist = False

    #Gets tracking number from user
    strTrackingNumber = input("What is the Tracking Number of the Package you wish to Delete? : ")

    with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:

        #Open database and converts the row of TrackingNumber into a list
        strQuery = "SELECT TrackingNumber FROM Packages"
        objCursor = conLogistics.cursor()
        objCursor.execute(strQuery)
        lstTrackingNumbers = objCursor.fetchall()

        #Iterates through the list to find the correct number if available
        for objTrackingNumber in lstTrackingNumbers:

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
                print(f"Package {strTrackingNumber} was deleted.")
                strContinue = input("Press enter to continue.")
            else:
                print("No Package was Deleted.")
                strContinue = input("Press enter to continue.")

        else:
            print("There was no package with that tracking number. Please try again.")
            strContinue = input("Press enter to continue.")
    conLogistics.close()

#Record
def recordArrivalOfPackage():

    strTrackingNumber = input("Enter the Tracking Number of the Package you wish to Record the Arrival of: ")
    if strTrackingNumber == "":
        print("Tacking Number cannot be blank! Please try again.")
        strTrackingNumber = input("Enter the Tracking Number of the Package you wish to Record the Arrival of: ")

    print("\n-----Facility-IDs-----")
    print("TN01 - Cookeville, TN")
    print("NJ02 - Jersey City, NJ")
    print("KS01 - Kansas City, KS")
    print("CA04 - Los Angeles, CA")
    print("ID01 Sioux City, ID")
    print("----------------------\n")

    strFacilityID = input("Enter the Facility ID of the Facility that the package has arrived to: ")
    if strFacilityID != "TN01" and strFacilityID != "NJ02" and strFacilityID != "KS01" and strFacilityID != "CA04" and strFacilityID != "ID01":
        print("Invalid FacilityID. Please try again.")
        strContinue = input("Press enter continue.")
    else:
        with sqlite3.connect("SwollenHippoLogistics_Sample.db") as conLogistics:
            #Prepared statement
            #Question marks align with the values being inserted
            strQuery = f"INSERT INTO TrackingHistory VALUES ((SELECT MAX(TrackingID) + 1 FROM TrackingHistory),?,?,?)"

            tupValues = (strTrackingNumber,strFacilityID,strCurrentTime)
            objCursor = conLogistics.cursor()
            #Using the tupValues
            objCursor.execute(strQuery,tupValues)

            conLogistics.commit()
            print(f"Package {strTrackingNumber}'s arrival time and location have been recorded.")
            strContinue = input("Press enter to continue.")
        conLogistics.close()

#Main Menu
def mainMenu():

    print("\n----------------------------------------Swollen-Hippo-Logistics----------------------------------------")
    print("1. Create a new package shipment.")
    print("2. View the shipping information for an existing package (Including the tracking history of a package).")
    print("3. Update the shipping information for an existing package.")
    print("4. Delete an existing package.")
    print("5. Record the arrival of a package at a regional shipping facility.")
    print("6. Exit the application.")
    print("-------------------------------------------------------------------------------------------------------")

    strChoice = input("Which menu option would you like to do (1-6): ")

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
        recordArrivalOfPackage()
        mainMenu()
    #Exit
    elif strChoice == "6":
        print("Exiting the application. Have a nice day!")
    else:
        print("Invalid Menu Selection. Please Try Again.")
        mainMenu()
#End of Global Functions

#Calls the main menu
mainMenu()
