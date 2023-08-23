#coffee shop managment application

import sqlite3

###general use programs###

#query
def query(sql,data):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(sql,data)
        db.commit()

#search data
def search_data(tableName,searchDataFieldName, searchDataValue, returnDataFieldName):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select {0} from {1} where {2}=?".format(returnDataFieldName, tableName, searchDataFieldName), (searchDataValue,))
        returnDataValues = cursor.fetchall()
    return returnDataValues
#search entries
def search_entry(tableName, searchDataFieldName, searchDataValue):
    with sqlite3.connect("coffee_shop.db") as db:
        cursor = db.cursor()
        cursor.execute("select * from {0} where {1}=?".format(tableName, searchDataFieldName), (searchDataValue,))
        returnEntries = cursor.fetchall()
    return returnEntries

###customer manangement###

#add customer
def add_customer(FirstName, LastName, Street, Town, PostCode, TelephoneNumber, EmailAddress):
    sql = "insert into Customer (FirstName, Lastname, Street, Town, PostCode, TelephoneNumber, EmailAddress) values (?,?,?,?,?,?,?)"
    query(sql, [FirstName, LastName, Street, Town, PostCode, TelephoneNumber, EmailAddress])
        
#update customer
def update_customer(CustomerID, dataFieldName, updateData):
    sql = "update Customer set {0}=? where CustomerID=?".format(dataFieldName)
    data = (updateData, CustomerID)
    query(sql, data)



#delete customer
def delete_customer(CustomerID):
    sql = "delete from Customer where CustomerID=?"
    data = (CustomerID,)
    query(sql, data)

###customerorder management###

#add customerorder
def add_customer_order(Date, Time, CustomerID):
    sql = "insert into CustomerOrder (Date, Time, CustomerID) values (?,?,?)"
    query(sql, (Date, Time, CustomerID))

#update customerorder
def update_customer_order(OrderID, dataFieldName, updateData):
    sql = "update CustomerOrder set {0}=? where OrderID=?".format(dataFieldName)
    data = (updateData, OrderID)
    query(sql, data)

#delete customerorder
def delete_customer_order(OrderID):
    sql = "delete from CustomerOrder where OrderID=?"
    data = (OrderID,)
    query(sql, data)

###orderitem management###

#add orderitem
def add_order_item(OrderID, ProductID, Quantity):
    sql = "insert into OrderItem (OrderID, ProductID, Quantity) values (?,?,?)"
    data = (OrderID, ProductID, Quantity)
    query(sql, data)
    
#update orderitem
def update_order_item(OrderItemID, dataFieldName, updateData):
    sql = "update OrderItem set {0}=? shere OrderItemID=?".format(dataFieldName)
    data = (updateData, OrderItemID)
    query(sql, data)
    
#delete orderitem
def delete_order_item(OrderItemID):
    sql = "delete from OrderItem where OrderItemID=?"
    data = (OrderItemID,)
    query(sql, data)
    
###product management###

#add product
def add_product(Name, Price, ProductTypeID):
    sql = "insert into Product (Name, Price, ProductTypeID) values (?,?,?)"
    data = (Name, Price, ProductTypeID)
    query(sql, data)

#update product
def update_product(ProductID, dataFieldName, updateData):
    sql = "update Product set {0}=? where ProductID=?".format(dataFieldName)
    data = (updateData, ProductID)
    query(sql, data)
    
#delete product
def delete_product(ProductID):
    sql = "delete from Product where ProductID=?"
    data = (ProductID,)
    query(sql, data)

###ProductType management

#add ProductType
def add_product_type(Description):
    sql = "insert into ProductType (Description) values (?)"
    query(sql, (Description,))
#update ProductType
def update_product_type(ProductTypeID, dataFieldName, updateData):
    sql = "update ProductType set {0}=? where ProductTypeID=?".format(dataFieldName)
    data = (updateData, ProductTypeID)
    query(sql, data)

#delete ProductType
def delete_product_type(ProductTypeID):
    sql = "delete from ProductType where ProductTypeID=?"
    data = (ProductTypeID,)
    query(sql, data)

###UI###

#menu display
def display_menu(menulist):
    print("Options:")
    valid = False
    while valid == False:
        valid_inputs = []
        for i in range(len(menulist)):
            print(str(i + 1) +  ". " + menulist[i])
            valid_inputs.append(str(i + 1))
        response = input("Select a number option: ")
        for i in valid_inputs:
            if response == i:
                valid = True
                return response
        print("invalid option\n")

#validation
#integers:
def int_valid(string):
    for i in string:
        if not 48 <= ord(i) <= 57:
            return False
    return True

def real_valid(string):
    for i in string:
        if (not 48 <= ord(i) <= 57) and i != ".":
            return False
    return True

#main menu
def main_menu():
    print("Main Menu")
    print("Please select an action")
    action = display_menu(["Add Entry", "Search data", "Update data", "Delete entry"])
    print("Please select an area")
    table = display_menu(["Customer", "Product Type", "Product", "CustomerOrder", "OrderItem"])
    if action == "1": #adding an entry
        if table == "1": #customer entry
            repeat = True
            while repeat:
                fname = input("Please enter customer's First Name: ")
                lname = input("Please enter customer's Last Name: ")
                street = input("Please enter customer's Street: ")
                town = input("Please enter customer's Town: ")
                postcode = input("Please enter customer's Post Code: ")
                phonenumber = input("Please enter customers Telephone Number: ")
                email = input("Please enter customer's Email Address: ")
                print("\nPlease confirm:\nFirst Name: {0} \nLast Name: {1}\nStreet: {2}\nTown: {3}\nPost Code: {4} \nTelephone Number: {5}\nEmail Address: {6}".format(fname,lname,street,town,postcode,phonenumber,email))
                correct = input("is this correct? (y/n) ")
                if correct == "y":
                    add_customer(fname, lname, street, town, postcode, phonenumber, email)
                    repeat = False
                else:
                    print("\nOK\n")
        elif table == "2": #product type entry
            repeat = True
            while repeat:
                description = input("Please enter Description: ")
                print("\nPlease confirm: \nDescription: {0}".format(description))
                correct = input("is this correct(y/n) ")
                if correct == "y":
                    add_product_type(description)
                    repeat = False
                else:
                    print("\nOK\n")
        elif table == "3": #product entry
            repeat = True
            while repeat:
                name = input("Please enter product name: ")
                price = input("Please enter product price: ")
                producttypeid = input("Please enter product's ProductTypeID")
                if real_valid(price) and int_valid(producttypeid):
                    print("\nPlease confirm:\nName: {0}\nPrice: {1}\nProductTypeID{2}".format(name,price,producttypeid))
                    correct = input("Is this correct? (y/n) ")
                    if correct == "y":
                        add_product(name, float(price), int(producttypeid))
                        repeat = False
                    else:
                        print("\nOK\n")
                else:
                    print("Invalid Input")
        elif table == "4": #order entry
            repeat = True
            while repeat:
                date = input("Please enter the order Date: ")
                time = input("Please enter the order Time: ")
                customerid = input("Please enter the CustomerID: ")
                if int_valid(customerid):
                    print("Please confirm:\nDate: {0}\nTime: {1}\nCustomerID: {2}".format(date, time, customerid))
                    correct = input("Is this correct? (y/n) ")
                    if correct == "y":
                        add_customer_order(date, time, int(customerid))
                    else:
                        print("\nOK\n")
                else:
                    print("Invalid Input")
        elif table == "5":
            repeat = True
            while repeat:
                orderid = input("Please enter the OrderID: ")
                productid = input("Please enter the ProductID: ")
                quantity = input("Please enter the Quantity: ")
                if int_valid(orderid) and int_valid(productid) and int_valid(quantity):
                    print("Please confirm:\nOrderID: {0}\nProductID: {1}\nQuantity: {2}".format(orderid, productid, quantity))
                    correct = input("Is this correct? (y/n) ")
                    if correct == "y":
                        add_order_item(int(orderid), int(productid), int(quantity))
    elif action == "2": #searching 
        if table == "1": #search customer
            repeat = True
            column_list = ["CustomerID", "FirstName", "LastName", "Street", "Town", "PostCode", "TelephoneNumber", "EmailAddress"]
            while repeat:
                print("Which column will you use to search?")
                choice = display_menu(column_list)
                print(choice)
                column = column_list[int(choice) - 1]
                print(column)
                search_value = input("Please enter your search data: ")
                if choice == "1":
                    if not int_valid(search_value):
                        print("invalid input")
                    else:
                        repeat = False
                        entries = search_entry("Customer", column, int(search_value))
                else:
                    entries = search_entry("Customer", column, search_value)
                    repeat = False
            print("CustomerID    First Name    Last Name    Street    Town    Post Code    Telephone Number    Email Address")
            for entry in entries:
                print("{0}        {1}     {2}     {3}     {4}     {5}     {6}     {7}     ".format(entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7]))
        if table == "2": #search product type
            repeat = True
            column_list = ["ProductTypeID", "Description"]
            while repeat:
                print("Which column will you use to search?")
                choice = display_menu(column_list)
                column = column_list[int(choice) - 1]
                search_value = input("Please enter your search data: ")
                if choice == "1":
                    if not int_valid(search_value):
                        print("invalid input")
                    else:
                        repeat = False
                        entries = search_entry("ProductType", column, int(search_value))
                else:
                    entries = search_entry("ProductType", column, search_value)
                    repeat = False
            print("ProductTypeID        Description")
            for entry in entries:
                print("{0}            {1}".format(entry[0], entry[1]))
        if table == "3": #search product
            repeat = True
            column_list = ["ProductID", "Name", "Price", "ProductTypeID"]
            while repeat:
                print("Which column will you use to search?")
                choice = display_menu(column_list)
                column = column_list[int(choice)]
                search_value = input("Please enter your search data: ")
                if choice == "1" or choice == "4":
                    if not int_valid(search_value):
                        print("invalid input")
                    else:
                        repeat = False
                        entries = search_entry("Product", column, int(search_value))
                elif choice == "3":
                    if not real_valid(search_value):
                        print("invalid input")
                    else:
                        repeat = False
                        entries = search_entry("Product", column, float(search_value))
                else:
                    entries = search_entry("ProductType", column, search_value)
                    repeat = False
            print("ProductID     Name     Price     ProductTypeID")
            for entry in entries:
                print("{0}        {1}     {2}     {3}".format(entry[0], entry[1], entry[2], entry[3]))
        if table == "4": #search customer order
            repeat = True
            column_list = ["OrderID", "Date", "Time", "CustomerID"]
            while repeat:
                print("Which column will you use to search?")
                choice = display_menu(column_list)
                column = column_list[int(choice)]
                search_value = input("Please enter your search data: ")
                if choice == "1" or choice == "4":
                    if not int_valid(search_value):
                        print("invalid input")
                    else:
                        repeat = False
                        entries = search_entry("CustomerOrder", column, int(search_value))
                else:
                    entries = search_entry("CustomerOrder", column, search_value)
                    repeat = False
            print("OrderID     Date     Time     CustomerID")
            for entry in entries:
                print("{0}        {1}     {2}     {3}".format(entry[0], entry[1], entry[2], entry[3]))
        if table == "5": #search order item
            repeat = True
            column_list = ["OrderItemID", "OrderID", "ProductID", "Quantity"]
            while repeat:
                print("Which column will you use to search?")
                choice = display_menu(column_list)
                column = column_list[int(choice)]
                search_value = input("Please enter your search data: ")
                if not int_valid(search_value):
                    print("invalid input")
                else:
                    repeat = False
                    entries = search_entry("OrderItem", column, int(search_value))
            print("OrderItemID     OrderID     ProductID     Quantity")
            for entry in entries:
                print("{0}        {1}     {2}     {3}".format(entry[0], entry[1], entry[2], entry[3]))
    if action == "3": #update data
        if table == "1": #update customer
            column_list = ["CustomerID", "FirstName", "LastName", "Street", "Town", "PostCode", "TelephoneNumber", "EmailAddress"]
            customerid = input("Enter CustomerID: ")
            print("Which column do you want to update?")
            choice = display_menu(column_list)
            column = column_list[int(choice - 1)]
            updatedata = input("Enter new data value: ")
            if int_valid(customerid):
                if choice == "1":
                    if int_valid(updatedata):
                        update_customer(int(customerid), column, int(updatedata))
                    else:
                        print("Invalid Input")
                else:
                    update_customer(int(customerid), column, updatedata)
            else:
                print("invalid input")
        if table == "2": #update product type
            column_list = ["ProductTypeID", "Description"]
            producttypeid = input("Enter ProductTypeID: ")
            print("Which column do you want to update?")
            choice = display_menu(column_list)
            column = column_list[int(choice - 1)]
            updatedata = input("Enter new data value: ")
            if int_valid(producttypeid):
                if choice == "1":
                    if int_valid(updatedata):
                        update_product_type(int(producttypeid), column, int(updatedata))
                    else:
                        print("Invalid Input")
                else:
                    update_customer(int(producttypeid), column, updatedata)
            else:
                print("invalid input")
        if table == "3": #update product
            column_list = ["ProductID", "Name", "Price", "ProductTypeID"]
            productid = input("Enter ProductID: ")
            print("Which column do you want to update?")
            choice = display_menu(column_list)
            column = column_list[int(choice - 1)]
            updatedata = input("Enter new data value: ")
            if int_valid(customerid):
                if choice == "1" or choice == "4":
                    if int_valid(updatedata):
                        update_product(int(productid), column, int(updatedata))
                    else:
                        print("Invalid Input")
                elif choice == "3":
                    if real_valid(updatedata):
                        update_product(int(productid), column, float(updatedata))
                    else:
                        print("Invalid Input")
                else:
                    update_customer(int(productid), column, updatedata)
            else:
                print("invalid input")
        if table == "4": #update customerorder
            column_list = ["OrderID", "Date", "Time", "CustomerID"]
            orderid = input("Enter OrderID: ")
            print("Which column do you want to update?")
            choice = display_menu(column_list) #user choosing column
            column = column_list[int(choice - 1)] #getting column from list
            updatedata = input("Enter new data value: ")
            if int_valid(orderid): 
                if choice == "1" or choice == "4":
                    if int_valid(updatedata):
                        update_customer(int(orderid), column, int(updatedata))
                    else:
                        print("Invalid Input")
                else:
                    update_customer(int(orderid), column, updatedata)
            else:
                print("invalid input")
        if table == "5": #update orderitem
            column_list = ["OrderItemID", "OrderID", "ProductID", "Quantity"]
            orderitemid = input("Enter OrderItem: ")
            print("Which column do you want to update?")
            choice = display_menu(column_list)
            column = column_list[int(choice - 1)]
            updatedata = input("Enter new data value: ")
            if int_valid(orderitemid) and int_valid(updatedata):
                update_order_item(int(orderitemid), column, int(updatedata))
            else:
                print("Invalid Input")
        if action == "4": #deleting
            if table == "1": #customer
                customerid = input("Enter CustomerID: ")
                if int_valid(customerid):
                    delete_customer(customerid)
                else:
                    print("Invalid Input")
            elif table == "2": #producttype
                producttypeid = input("Enter ProductTypeID: ")
                if int_valid(producttypeid):
                    delete_product_type(producttypeid)
                else:
                    print("Invalid Input")
            elif table == "3": #product
                productid = input("Enter ProductID: ")
                if int_valid(productid):
                    delete_product(productid)
                else:
                    print("Invalid Input")
            elif table == "4": #customerorder
                orderid = input("Enter OrderID: ")
                if int_valid(orderid):
                    delete_product(orderid)
                else:
                    print("Invalid Input")
            elif table == "5": #orderitem
                orderitemid = input("Enter OrderItemID: ")
                if int_valid(orderitemid):
                    delete_product(orderitemid)
                else:
                    print("Invalid Input")
    

if __name__ == "__main__":
    main_menu()