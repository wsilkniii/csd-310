#Group name: Charlie Group
#Members: Jacob Breault, Angela Perkins, Skyler Millburn, William Silknitter III, Cameron Frison
#7/11/2021
#Module 10.3 ADD RECORDS Outland Adventures Script

"""import statements"""
import mysql.connector
from datetime import datetime
from mysql.connector import errorcode

"""database config object"""
config = {
    "user": "root",
    "password": "!SilknitterI3#",
    "host": "127.0.0.1",
    "database": "outland_adventures",
    "raise_on_warnings": True
}

""" try/catch block for handling potential MySQL database errors """ 
try:
    
    
    db = mysql.connector.connect(**config) # connect to outland_adventures database.
    cursor = db.cursor()
    
    """Truncate all tables; makes sure we have empty tables before entering data"""
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE inventory")
    cursor.execute("TRUNCATE employee_trek_history")
    cursor.execute("TRUNCATE trek_history")
    cursor.execute("TRUNCATE trek")
    cursor.execute("TRUNCATE orders")
    cursor.execute("TRUNCATE employees")
    cursor.execute("TRUNCATE customers")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    
    """Executemany values into customers table"""
    customerSQL = "INSERT INTO customers(f_name, l_name, address, city, state, zip_code, phone) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    customerRecord = [
        ('John', 'Smith', '123 Apple Street', 'Bigcity', 'Indiana', '12345', '123-456,7890'),
        ('Lily', 'Smith', '123 Apple Street', 'SmallCity', 'Kentucky', '54321', '098-765-4321'),
        ('Jake', 'Johnson', '456 Pear Ave', 'MedCity', 'Ohio', '44444', '111-111-1111'),
        ('Mary', 'Lee', '555 Orange Rd', 'OtherCity', 'Florida', '22222', '222-222-2222'),
        ('Thomas', 'Jones', '999 West St', 'Sidecity', 'Arizona', '66666', '999-999-9999'),
        ('Isacc', 'Lee', '555 Orange Rd', 'OtherCity', 'Florida', '22222', '222-222-2222')
    ]
    
    cursor.executemany(customerSQL, customerRecord)
    
    """Display all from customers table"""
    cursor.execute("SELECT * FROM customers")
    customer = cursor.fetchall()
    
    print(" -- DISPLAYING ENTRIES FROM CUSTOMER TABLE -- \n\n")
    for customers in customer:
        print(customers)
        print("\n")
    
    
    """Executemany values into employees table"""
    now = datetime.now()
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    employeeSQL = "INSERT INTO employees(f_name, l_name, date_of_birth, title, supervisor_id) VALUES (%s, %s, %s, %s, %s)"
    employeeRecord = [
        ('Luke', 'Johnson', formatted_date, 'Boss', 1),
        ('Bryan', 'Smith', formatted_date, 'Associate', 2),
        ('John', 'Jones', formatted_date, 'Manager', 3),
        ('Percy', 'Smith', formatted_date, 'Marketing', 4),
        ('Ash', 'Williams', formatted_date, 'Human Resources', 5),
        ('Terrance', 'Fletcher', formatted_date, 'Co-Boss', 6),
    ]
    
    cursor.executemany(employeeSQL, employeeRecord)
    
    """Display all from customers table"""
    cursor.execute("SELECT * FROM employees")
    employee = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM EMPLOYEE TABLE -- \n\n")
    for employees in employee:
        print(employees)
        print("\n")
    
    
    """Executemany values into trek table"""
    trekSQL = "INSERT INTO trek(trek_name, country, requires_visa, required_immunizations) VALUES (%s, %s, %s, %s)"
    trekRecord = [
        ('Trek 1', 'Canada', 1, 1),
        ('Trek 2', 'U.S.A.', 1, 1),
        ('Trek 3', 'Mexico', 1, 1),
        ('Trek 4', 'Quebec', 1, 1),
        ('Trek 5', 'U.S.A.', 1, 1),
        ('Trek 6', 'Canada', 1, 1)
    ]
    
    cursor.executemany(trekSQL, trekRecord)
    
    """Display all from trek table"""
    cursor.execute("SELECT * FROM trek")
    trek = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM TREK TABLE -- \n\n")
    for treks in trek:
        print(treks)
        print("\n")
    
    
    """Executemany values into orders table"""
    orderSQL = "INSERT INTO orders(customer_id, gear_id, quantity, order_cost, order_date) VALUES (%s, %s, %s, %s, %s)"
    orderRecord = [
        (1, 1, 10, 50, formatted_date),
        (2, 2, 20, 100, formatted_date),
        (3, 3, 3, 10, formatted_date),
        (4, 4, 7, 110, formatted_date),
        (5, 5, 11, 100, formatted_date),
        (6, 6, 14, 200, formatted_date)
    ]
    
    cursor.executemany(orderSQL, orderRecord)
    
    """Display all from orders table"""
    cursor.execute("SELECT * FROM orders")
    order = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM ORDERS TABLE -- \n\n")
    for orders in order:
        print(orders)
        print("\n")
    
    
    
    """Executemany values into inventory table"""
    inventorySQL = "INSERT INTO inventory(gear_id, gear_name, for_rent, purchase_date) VALUES (%s, %s, %s, %s)"
    inventoryRecord = [
        (1, 'Boots', 1, formatted_date),
        (2, 'Lantern', 1, formatted_date),
        (3, 'Tent', 1, formatted_date),
        (4, 'Ligher', 1, formatted_date),
        (5, 'Hydro Flasks', 1, formatted_date),
        (6, 'Backpack', 1, formatted_date)
    ]
    
    cursor.executemany(inventorySQL, inventoryRecord)
    
    """Display all from orders table"""
    cursor.execute("SELECT * FROM inventory")
    inventory = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM INVENTORY TABLE -- \n\n")
    for stock in inventory:
        print(stock)
        print("\n")
    
    
    """Executemany values into trek_history table"""
    trekHistorySQL = "INSERT INTO trek_history(customer_id, trek_name, trip_cost, trip_date) VALUES (%s, %s, %s, %s)"
    trekHistoryRecord = [
        (1, 'Trek 1', 500, formatted_date),
        (2, 'Trek 2', 300, formatted_date),
        (3, 'Trek 3', 200, formatted_date),
        (4, 'Trek 4', 175, formatted_date),
        (5, 'Trek 5', 1000, formatted_date),
        (6, 'Trek 6', 600, formatted_date)
    ]
    
    cursor.executemany(trekHistorySQL, trekHistoryRecord)
    
    """Display all from trek_history table"""
    cursor.execute("SELECT * FROM trek_history")
    trek_history = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM TREK HISTORY TABLE -- \n\n")
    for trekHis in trek_history:
        print(trekHis)
        print("\n")
    
    
    
    """Executemany values into employee_trek_history table"""
    empTrekSQL = "INSERT INTO employee_trek_history(trek_history_id, employee_id, supervisor_id) VALUES (%s, %s, %s)"
    empTrekRecord = [
        (1, 1, 1),
        (2, 2, 2),
        (3, 3, 3),
        (4, 4, 4),
        (5, 5, 5),
        (6, 6, 6)
    ]
    
    cursor.executemany(empTrekSQL, empTrekRecord)
    
    """Display all from employee_trek_history table"""
    cursor.execute("SELECT * FROM employee_trek_history")
    empTrek = cursor.fetchall()
    
    print("\n\n -- DISPLAYING ENTRIES FROM EMPLOYEE TREK HISTORY TABLE -- \n\n")
    for history in empTrek:
        print(history)
        print("\n")
    
    
    
    db.commit()
    
except mysql.connector.Error as err:
    """ on error code """

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()
    