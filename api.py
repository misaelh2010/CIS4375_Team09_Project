import mysql.connector
from mysql.connector import Error
import hashlib
import datetime
import time
import flask  # , werkzeug
from flask import jsonify, make_response
from flask import request, make_response
from flask import request, jsonify
# from sql import create_connection
# from sql import execute_read_query
# from sql import execute_query
from datetime import datetime


def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name

        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occured.")
    return connection

# function that will be called in the main file to carry out the query in the app.route in which it is used in


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}'")

# i am planning to use this function with the app routes that pertain to the logs table


def execute_read_query(connection, query):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
    except Error as e:
        print(f"The error '{e}' occured")


# setting up the application
app = flask.Flask(__name__)  # sets up the application
app.config["DEBUG"] = True  # allow to show error in browser

@app.route('/employees', methods = ['GET'])
def employees():
    # try: 
    #     token = current_tokens[curuser.get_current_user()]
    # except:
    #     return 'No Active User Detected'
    # if float(token) > time.time():
        sql = """
        SELECT e.first_name, e.last_name, e.start_date, e.end_date, e.emp_status, r.role_name
        FROM employees e
        JOIN roles r
        ON e.role_id = r.role_id;
        """
        results = execute_read_query(conn, sql)

        sql = """
        SELECT * FROM States
        """
        state_results = execute_read_query(conn, sql)
        return jsonify(state_results, results)

app.run()
