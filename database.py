import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@123",
        database="quiz_db"
    )

def execute_query(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    conn.commit()
    conn.close()

def fetch_data(query, params=None):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    result = cursor.fetchall()
    conn.close()
    return result
