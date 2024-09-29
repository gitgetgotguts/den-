import psycopg2
# pg_ctl -D /var/lib/postgres/data1 -l logfile start



# Database connection parameters
host = "localhost"  # or your PostgreSQL server address
port = "5432"       # default PostgreSQL port
dbname = "etl"  # the name of your database
user = "postgres"    # your PostgreSQL username
password = "etl"  # your PostgreSQL password

try:
    # Establish a connection to the database
    connection = psycopg2.connect(
        host=host,
        port=port,
        dbname=dbname,
        user=user,
        password=password
    )

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a query (optional)
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print("Connected to database:", db_version)

except Exception as e:
    print("Error while connecting to PostgreSQL:", e)
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()

