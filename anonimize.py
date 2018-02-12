import psycopg2
import os
from faker import Faker
try:
    conn = psycopg2.connect(dbname=os.getenv('POSTGRES_DB'), user=os.getenv('POSTGRES_USER'), host='localhost', password= os.getenv('POSTGRES_PASSWORD'))
    cur = conn.cursor()
    cur.execute("""SELECT id from x""")
    rows = cur.fetchall()
    fake = Faker()
    for row in rows:
        cur.execute("""
        update
        doctors
        set(name, surname, number, address_line_1, email) =
        (%s, %s, %s, %s, %s)
        where  id = %s
        """, (fake.first_name(), fake.last_name(), fake.phone_number(), fake.address(), fake.safe_email(), row[0]))
        conn.commit()
    print "x anomnimized"
    cur.execute("""SELECT id from y""")
    rows = cur.fetchall()
    for row in rows:
        cur.execute("""
           update
           patients
           set(name, surname, email) =
           (%s, %s, %s)
           where  id = %s
           """, (fake.first_name(), fake.last_name(),  fake.safe_email(), row[0]))
        conn.commit()
    cur.close()
    conn.close()
    print "Y anomnimized"
except:
    print "Something went wrong"
