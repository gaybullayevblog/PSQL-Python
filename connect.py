# Note: the module name is psycopg, not psycopg3
import psycopg

# Connect to an existing database
with psycopg.connect("dbname=postgres user=postgres host=localhost port=5432 password=080199") as conn:

    # Open a cursor to perform database operations
    with conn.cursor() as cur:

        # Execute a command: this creates a new table
        # cur.execute("""
        #     CREATE TABLE test (
        #         id serial PRIMARY KEY,
        #         num integer,
        #         data text)
        #     """)

        # Pass data to fill a query placeholders and let Psycopg perform
        # the correct conversion (no SQL injections!)
        # cur.execute(
        #     "INSERT INTO test (num, data) VALUES (%s, %s)",
        #     (100, "abc'def"))

        # Query the database and obtain data as Python objects.
        cur.execute("SELECT * FROM users")
        
        # version = cur.fetchone()
        # print(version)

        # rows = cur.fetchall()
        # for row in rows:
        #     print(row)

        rows = cur.fetchmany()
        # for row in rows:
        #     print(row)
        print(rows)

        # You can use `cur.fetchmany()`, `cur.fetchall()` to return a list
        # of several records, or even iterate on the cursor
        # for record in cur:
        #     print(record)

        # Make the changes to the database persistent
        conn.commit()