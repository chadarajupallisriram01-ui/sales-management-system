import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import sqlite3 as sq

path = os.path.join(os.getcwd(),"Database.db")

def get_connection():
    return sq.connect("Database.db",check_same_thread=False)
def create_tables():
    conn = get_connection()
    cur = conn.cursor()

    # Employee
    cur.execute("""Create Table If not exists Employee(
                Mobile integer primary key,
                Name text not null,
                Password text not null,
                Role text check(Role in("Admin","Employee","Developer")),
                created_at timestamp
                )""")
    # Sales
    cur.execute("""Create Table If not exists Sales(
                sale_id integer primary key Autoincrement,
                Product_id integer not null,
                Product_Name text not null,
                Product_Category Text not null,
                Quantity Integer,
                Usp integer not null,
                Ucp integer not null,
                Tsp integer not null,
                tcp integer not null,
                Revenue integer not null,
                Rent Integer not null,
                Expenditure integer not null,
                Gsp Integer not null,
                profit integer not null,
                Mobile Text not null,
                created_at timestamp
                )""")
    conn.commit()
    conn.close()
    return "✅ Database successfully connected"
print(create_tables())
