import greeting
import choice 
from time import sleep
import sqlite3

connection = sqlite3.connect("employee.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE employee (id INTEGER, name TEXT, salary INTEGER , designation TEXT , workinghours INTEGER)")

greeting.start_greet()
greeting.greet()
# sql_connector.connect_database()
choice.choose()

greeting.copyright()
