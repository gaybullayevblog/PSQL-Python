# Note: the module name is psycopg, not psycopg3
import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost port=5432 password=umid8505") as conn:

    conn.autocommit = True

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # query to create a database
        sql = "DROP DATABASE your_db"
        

        # executing above query
        cur.execute(sql)
        print("Drop Database!!")