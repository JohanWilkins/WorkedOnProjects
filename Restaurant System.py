# Class to create orders to prepare a bill
class TableOrders:
    def __init__(self, table_number, item_ordered, amount, bill):
        self.table_number = table_number
        self.item_ordered = item_ordered
        self.amount = amount
        self.bill = bill


# Class to create table objects (For checks and part of the creation of bills
class Table:
    def __init__(self, table_number, waiter_assign, customer_count, bill_total):
        self.table_number = table_number
        self.waiter_assign = waiter_assign
        self.customer_count = customer_count
        self.bill_total = bill_total


# Function to add customers to a table
def cust_add():
    global customer_amount
    if table_cust_add == '1' and user_name == table_1.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_1.customer_amount = customer_amount
    elif table_cust_add == '2' and user_name == table_2.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_2.customer_amount = customer_amount
    elif table_cust_add == '3' and user_name == table_3.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_3.customer_amount = customer_amount
    elif table_cust_add == '4' and user_name == table_4.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_4.customer_amount = customer_amount
    elif table_cust_add == '5' and user_name == table_5.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_5.customer_amount = customer_amount
    elif table_cust_add == '6' and user_name == table_6.waiter_assign:
        customer_amount = input("How many customers are seated at the table? ")
        table_6.customer_amount = customer_amount


# Function to print tables that are available to the user that is logged in
def table_menu():
    if user_name in table_1.waiter_assign:
        print("1. Table 1")
    if user_name in table_2.waiter_assign:
        print("2. Table 2")
    if user_name in table_3.waiter_assign:
        print("3. Table 3")
    if user_name in table_4.waiter_assign:
        print("4. Table 4")
    if user_name in table_5.waiter_assign:
        print("5. Table 5")
    if user_name in table_6.waiter_assign:
        print("6. Table 6")


# Function to add orders to a table
def add_order_menu():
    global key_test, sum_of_price, amount_ordered
    if cust_choice == '1':
        key_test = 'Coke'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Coke'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '2':
        key_test = 'Fanta'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Fanta'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '3':
        key_test = 'Sprite'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Sprite'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '4':
        key_test = 'Garlic Snails'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Garlic Snails'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '5':
        key_test = 'Calamari'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Calamari'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '6':
        key_test = 'Wings'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Wings'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '7':
        key_test = 'Steak'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Steak'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '8':
        key_test = 'Chicken'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Chicken'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '9':
        key_test = 'Pork'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Pork'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '10':
        key_test = 'Ice-cream'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Ice-cream'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == '11':
        key_test = 'Waffle'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Waffle'] * amount_ordered
            return sum_of_price, amount_ordered, key_test
    elif cust_choice == 'Cake':
        key_test = 'Cake'
        if key_test in stock_list:
            amount_ordered = int(input("How many items do you want to add? "))
            sum_of_price = stock_list['Cake'] * amount_ordered
            return sum_of_price, amount_ordered, key_test


# Function to prepare a bill. It also automates the printing of a bill with the correct title to the folder in the
# program.


def bill_preparation():
    global cashup_count_1, cashup_count_2, cashup_count_3, cashup_count_4, cashup_count_5, cashup_count_6
    dash_line = "-" * 65
    item, quantity, price = 'Item', 'Quantity', 'Price'
    try:  # Loads the data from the orders for processing to a bill
        if prepare_bill == '1':
            table = table_1
            table_order = table_order_1
            cashup_count_1 = table_1.bill_total
            cashup_count = cashup_count_1
        elif prepare_bill == '2':
            table = table_2
            table_order = table_order_2
            cashup_count_2 = table_2.bill_total
            cashup_count = cashup_count_2
        elif prepare_bill == '3':
            table = table_3
            table_order = table_order_3
            cashup_count_3 = table_3.bill_total
            cashup_count = cashup_count_3
        elif prepare_bill == '4':
            table = table_4
            table_order = table_order_4
            cashup_count_4 = table_4.bill_total
            cashup_count = cashup_count_4
        elif prepare_bill == '5':
            table = table_5
            table_order = table_order_5
            cashup_count_5 = table_5.bill_total
            cashup_count = cashup_count_5
        elif prepare_bill == '6':
            table = table_6
            table_order = table_order_6
            cashup_count_6 = table_6.bill_total
            cashup_count = cashup_count_6
        else:
            raise ValueError("Invalid table number")
        # Process that automates the printing of the bill to a txt file with the correct name. It also displays the bill
        # in console
        with open(f"table{prepare_bill}_bill.txt", "w") as file:
            file.write(
                f"{dash_line}\nThe bill for Table {prepare_bill}:\n {item : >20}{quantity: >20}{price : >20}\n")
            print(
                f"{dash_line}\nThe bill for Table {prepare_bill}:\n {item : >20}{quantity: >20}{price : >20}\n")
            for contents_bill in table_order:
                table.bill_total += contents_bill.bill
                file.write(
                    f"{contents_bill.item_ordered: >21}{contents_bill.amount: ^30} R:{contents_bill.bill: ^10}\n")
                file.write(f"The total of your order was R {table.bill_total}\n")
                file.write(f"You have been served by {table.waiter_assign}\n")
                file.write(f"{dash_line}\n")
                # Prints the bill to the console
                print(f"{contents_bill.item_ordered: >21}{contents_bill.amount: ^30} R:{contents_bill.bill: ^10}\n")
                print(f"The total of your order was R {table.bill_total}\n")
                print(f"You have been served by {table.waiter_assign}\n")
                print(f"{dash_line}\n")

        cashup_count = table.bill_total
        return cashup_count
    except TypeError:
        print("Do not enter letters. Please use numbers")


# Declarations to create tables as class objects
table_1 = Table(1, 'Default', 0, 0)
table_2 = Table(2, 'Default', 0, 0)
table_3 = Table(3, 'Default', 0, 0)
table_4 = Table(4, 'Default', 0, 0)
table_5 = Table(5, 'Default', 0, 0)
table_6 = Table(6, 'Default', 0, 0)
# Empty table orders that will be populated with the orders that the people make.
table_order_1 = []
table_order_2 = []
table_order_3 = []
table_order_4 = []
table_order_5 = []
table_order_6 = []

total_sale = 0
menu_open = True  # Statement that keeps the menu continuously running

while menu_open:
    print("Welcome to Highlands Cafe\n\n")
    menu_choice = input("1. Login\n2. Exit\n")
    if menu_choice == '1':
        user_name = input('User login\n\nPlease enter a username: ').capitalize()
        try:
            input_password = int(input("Please enter a password: "))
        except ValueError:
            print("Incorrect input. Please use letters")
        try:  # Username and password tester. Error checks for incorrect type values as well
            with open('Login.txt', 'r') as f:
                for line in f:
                    user, password = line.strip().split(",")
                    user = user.capitalize()
                    password = int(password)
                    try:
                        if user_name == user and input_password == password:
                            authorize = True
                            break
                        elif user_name != user and input_password == password:
                            print("User Name is incorrect. Try again")
                            authorize = False
                            break
                        elif user_name == user and input_password != password:
                            authorize = False
                            print("Password is incorrect. Try Again")
                            break
                    except NameError:
                        authorize = False
        except IOError:
            print("The file cannot be found")

        while authorize:  # Loop for menu
            print("\nWelcome", user_name, "\nWhat would you like to do today?\n")
            user_choice = input("1. Assign Table\n2. Change Customers\n3. Add to Order\n4. Prepare "
                                "bill\n5. Complete Sale\n6. Cashup\n0. Log Out\n")
            try:  # Menu for assignment to a table. USed only if statements so it will check every table for condition
                if user_choice == '1':
                    print("Please select one of the available tables or press 0 to exit\n")
                    if table_1.waiter_assign == 'Default':
                        print("1.Table 1")
                    if table_2.waiter_assign == 'Default':
                        print("2.Table 2")
                    if table_3.waiter_assign == 'Default':
                        print("3.Table 3")
                    if table_4.waiter_assign == 'Default':
                        print("4.Table 4")
                    if table_5.waiter_assign == 'Default':
                        print("5.Table 5")
                    if table_6.waiter_assign == 'Default':
                        print("6.Table 6")
                    table_choice = input()
                    # if/else statements that allow a waiter to be assigned to a table.
                    if table_choice == '1':
                        if table_1.waiter_assign == 'Default':
                            table_1.waiter_assign = user_name
                            print("Table successfully assigned to ", table_1.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_1.waiter_assign)
                    elif table_choice == '2':
                        if table_2.waiter_assign == 'Default':
                            table_2.waiter_assign = user_name
                            print("Table successfully assigned to ", table_2.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_2.waiter_assign)
                    elif table_choice == '3':
                        if table_3.waiter_assign == 'Default':
                            table_3.waiter_assign = user_name
                            print("Table successfully assigned to ", table_3.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_3.waiter_assign)
                    elif table_choice == '4':
                        if table_4.waiter_assign == 'Default':
                            table_4.waiter_assign = user_name
                            print("Table successfully assigned to ", table_4.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_4.waiter_assign)
                    elif table_choice == '5':
                        if table_5.waiter_assign == 'Default':
                            table_5.waiter_assign = user_name
                            print("Table successfully assigned to ", table_5.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_5.waiter_assign)
                    elif table_choice == '6':
                        if table_6.waiter_assign == 'Default':
                            table_6.waiter_assign = user_name
                            print("Table successfully assigned to ", table_6.waiter_assign)
                            customer_input = input("Do you want to add customers to the table? y/n")
                        else:
                            print("The table is already assigned to", table_6.waiter_assign)
                    if customer_input.lower() == 'y':  # Allows the user to add customers to the table after assignment
                        table_menu()
                        table_cust_add = input("Select table to assign customers or 0 to exit")
                        cust_add()
                elif user_choice == '2':
                    table_menu()
                    select_table = input("Select Table to assign customers or 0 to exit: ")
                    cust_add()
                elif user_choice == '3':
                    stock_list = {}
                    try:
                        with open('Stock.txt', 'r') as f:  # Loads the items into a dictionary for easier print
                            for lines in f:
                                key, value = lines.strip().split(",")
                                stock_list[str(key)] = int(value)
                    except IOError:
                        print("The file cannot be found")

                    print("Select a table to add order to: \n")
                    table_menu()
                    add_order_table = input("Please select a table or 0 to exit\n")
                    print("Select an item from the list to add to order")
                    if add_order_table == '1':  # if/elif to add items to an order list for a particular table
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                        table_order_1.append(table_1_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Allows you to add extra items if customer wants more
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                    elif add_order_table == '2':  # Allows you to add items ordered
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_2_temp = TableOrders(2, key_test, amount_ordered, sum_of_price)
                        table_order_2.append(table_2_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Add more items if customer requests it
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                    elif add_order_table == '3':  # Allows you to add items
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_3_temp = TableOrders(3, key_test, amount_ordered, sum_of_price)
                        table_order_3.append(table_3_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Add more items if customer requests it
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                    elif add_order_table == '4':  # Allows you to add items ordered
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_4_temp = TableOrders(4, key_test, amount_ordered, sum_of_price)
                        table_order_4.append(table_4_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Add more items if customer requests it
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                    elif add_order_table == '5':  # Allows you to add items ordered
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_5_temp = TableOrders(5, key_test, amount_ordered, sum_of_price)
                        table_order_5.append(table_5_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Add more items if customer requests it
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                    elif add_order_table == '6':  # Allows you to add items ordered
                        item_number = 0
                        for x, y in stock_list.items():
                            item_number += 1
                            print(item_number, ".", x, "R", y)
                        cust_choice = input("Choose an item to add: ")
                        add_order_menu()
                        table_6_temp = TableOrders(6, key_test, amount_ordered, sum_of_price)
                        table_order_6.append(table_6_temp)
                        add_more_items = input("Add Another item? y/n: ")
                        if add_more_items == 'y':  # Add more items if customer requests it
                            item_number = 0
                            for x, y in stock_list.items():
                                item_number += 1
                                print(item_number, ".", x, "R", y)
                            cust_choice = input("Choose an item to add: ")
                            add_order_menu()
                            table_1_temp = TableOrders(1, key_test, amount_ordered, sum_of_price)
                            table_order_1.append(table_1_temp)
                            add_more_items = input("Add Another item? y/n: ")
                elif user_choice == '4':  # Preparation of bill using a function. Bill is added to .txt file
                    print("Select a table: ")
                    table_menu()
                    prepare_bill = input("Select a table or 0 to exit\n:")
                    bill_preparation()
                elif user_choice == '5':  # Option to clear tables after sales and add count to income for day
                    print("Select a table: ")
                    table_menu()
                    completion_select = input("Choose a table")
                    if completion_select == '1':  # Table 1 Clear
                        total_sale += table_1.bill_total
                        table_1 = Table(1, 'Default', 0, 0)
                        table_order_1.clear()
                        if table_1.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                    elif completion_select == '2':  # Table 2 Clear
                        total_sale += table_2.bill_total
                        table_2 = Table(2, 'Default', 0, 0)
                        table_order_2.clear()
                        if table_2.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                    elif completion_select == '3':
                        total_sale += table_3.bill_total  # Table 3 Clear
                        table_3 = Table(3, 'Default', 0, 0)
                        table_order_3.clear()
                        if table_3.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                    elif completion_select == '4':
                        total_sale += table_4.bill_total  # Table 4 Clear
                        table_4 = Table(1, 'Default', 0, 0)
                        table_order_4.clear()
                        if table_4.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                    elif completion_select == '5':
                        total_sale += table_5.bill_total  # Table 5 Clear
                        table_5 = Table(5, 'Default', 0, 0)
                        table_order_5.clear()
                        if table_5.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                    elif completion_select == '6':
                        total_sale += table_6.bill_total  # Table 6 clear
                        table_6 = Table(6, 'Default', 0, 0)
                        table_order_6.clear()
                        if table_6.waiter_assign == 'Default':
                            print("Table was successfully cleared")
                        else:
                            print("Table was not cleared")
                elif user_choice == '6':  # Displays the total money made for the day and clears it on request
                    print(f"Today we made R {total_sale}")
                    clear_daily_income = input("Do you wish to clear the daily total? y/n ").lower()
                    if clear_daily_income == 'y':
                        total_sale = int(0)
                elif user_choice == '0':  # Logout so other user can use system
                    print("Good Bye")
                    break
            except ValueError:
                print("Do not enter letter. Please use a number")
