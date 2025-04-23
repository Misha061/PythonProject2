import pyodbc

def get_connection():
    try:
        conn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};'
            'SERVER=localhost,3717;'
            'DATABASE=LoginDB;'
            'Trusted_Connection=yes;'
        )
        return conn
    except Exception as e:
        print("Connection error:", e)
        return None
