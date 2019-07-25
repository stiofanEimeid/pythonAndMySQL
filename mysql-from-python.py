import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (Modify this variable if running on another environment)

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')
                            
try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['Fred', 'Fred']
        #Prepare a string with the same number of placeholders as are in the list_of_names variable
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM FRIENDS WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
    