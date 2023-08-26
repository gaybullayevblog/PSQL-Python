import psycopg

with psycopg.connect("dbname=postgres user=postgres password=umid8505 port=5432") as conn:

    conn.autacommit = True

    with conn.carsor() as cur:

        sql = 'CREATE DATABASE my_db'

        cur.execute(sql)
        print('Databasa hes bein created successfully')
        
        conn.commit()