import pymysql.cursors

# Configure MySQL connection
def get_connection():
    return pymysql.connect(
        host="localhost",  # Replace with your DB host
        user="root",       # Replace with your username
        password="Abhishek@1259",       # Replace with your password
        database="task_manager",
        cursorclass=pymysql.cursors.DictCursor
    )
