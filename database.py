import psycopg2
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="0000",
    port=5432
)

cur = conn.cursor()

print("Database connection successful!")