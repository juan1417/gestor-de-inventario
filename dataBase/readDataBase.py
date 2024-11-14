import os
from dotenv import load_dotenv
import psycopg2

try:
    load_dotenv()
    
    dbname = os.getenv("DBName")
    user = os.getenv("user")
    password = os.getenv("password")
    host = os.getenv("host")
    port = os.getenv("port")

    print(f"DBName: {dbname}, User: {user}, Host: {host}, Port: {port}")

    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    print("Database opened successfully")
except Exception as e:
    print("I am unable to connect to the database")
    print(e)