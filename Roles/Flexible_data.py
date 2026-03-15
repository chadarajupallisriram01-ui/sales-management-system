import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
from Database import get_connection
from datetime import datetime,timedelta
from datetime import date 
import random
from faker import Faker
import string as s
import hashlib as h
phone = []
def Employee(n):
    n1 = int(n)
    fake = Faker("en-IN")
    for i in range(n1):
        name = fake.name()
        ph = random.randint(6000000000,9999999999)
        # password
        l =10
        ch = s.ascii_lowercase + s.ascii_uppercase + s.digits + s.punctuation
        pwd = ''.join(random.choice(ch) for i in range(l))
        phone.append(ph)
        hpwd = h.sha256(pwd.encode()).hexdigest()

        # Date
        today = date.today()
        start_date = datetime(2023,1,1)

        time = today - start_date.date()

        days = time.days

        random_days = random.randint(0,days)
        random_date = start_date + timedelta(days = random_days) 

        now = random_date.date()
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""Insert or Ignore into Employee(
                    Mobile,Name,Password,Created_at)values(?,?,?,?)
                    """,(ph,name,hpwd,now))

        cur.execute("""Insert or Ignore into Employee_Duplicate(
                    Mobile,Name,Password,Created_at
                    )values(?,?,?,?)""",(ph,name,pwd,now))
        conn.commit()
        conn.close()
    st.success("Data inserted Successfully..")
def Sales(n):
    n2 = int(n)
    fake = Faker()
    
    # Date

    electronics_products = {

        "Computers": {
            "Laptop": (40000, 120000),
            "Desktop": (30000, 90000),
            "Mini PC": (20000, 60000),
            "All-in-One PC": (35000, 80000)
        },

        "Mobile Devices": {
            "Smartphone": (8000, 100000),
            "Tablet": (10000, 70000),
            "Smartwatch": (2000, 40000),
            "E-Reader": (8000, 25000)
        },

        "Audio Devices": {
            "Headphones": (1000, 20000),
            "Earbuds": (800, 15000),
            "Bluetooth Speaker": (1500, 20000),
            "Soundbar": (5000, 50000)
        },

        "Computer Accessories": {
            "Mouse": (200, 3000),
            "Keyboard": (500, 5000),
            "Webcam": (1000, 8000),
            "USB Hub": (300, 2000)
        },

        "Storage Devices": {
            "External Hard Drive": (3000, 12000),
            "USB Flash Drive": (300, 2000),
            "Memory Card": (400, 3000),
            "SSD": (2500, 15000)
        },

        "Networking Devices": {
            "WiFi Router": (1500, 10000),
            "Modem": (1200, 6000),
            "Network Switch": (1500, 8000),
            "Range Extender": (1200, 5000)
        },

        "Display Devices": {
            "Monitor": (6000, 40000),
            "Projector": (15000, 100000),
            "Smart TV": (15000, 150000),
            "Digital Display": (20000, 120000)
        },

        "Gaming Devices": {
            "Gaming Console": (30000, 60000),
            "VR Headset": (20000, 90000),
            "Game Controller": (2000, 8000),
            "Gaming Keyboard": (1500, 10000)
        },

        "Camera Devices": {
            "Digital Camera": (20000, 120000),
            "Action Camera": (15000, 50000),
            "Web Camera": (1000, 8000),
            "Drone Camera": (30000, 200000)
        },

        "Power Devices": {
            "Power Bank": (500, 5000),
            "UPS": (2500, 15000),
            "Battery Charger": (500, 3000),
            "Extension Board": (300, 1500)
        }

    }
    for i in range(n2):
        P_id = random.randint(0,10000)
        start = datetime(2023,1,13)
        end = date.today()

        time  = end - start.date()
        days = time.days
        random_days = random.randint(5,days)
        random_date = start + timedelta(days = random_days)
        now = random_date.date()
        p_cat = random.choice(list(electronics_products.keys()))
        p_name = random.choice(list(electronics_products[p_cat].keys()))
        price_range = electronics_products[p_cat][p_name]
        usp = random.randint(price_range[0],price_range[1])
        qua = random.randint(1,1000)
        ucp = usp*0.4
        tsp = usp*qua
        tcp = ucp *qua
        rent = tcp * 0.4
        exp = tcp * 0.6
        gsp = tcp+rent+exp
        pro = gsp - exp
        ph = random.choice(phone)
        
        conn= get_connection()
        cur = conn.cursor()

        cur.execute("""insert or ignore into Sales(Product_id,Product_Name,Product_Category,Quantity,Usp,Ucp,Tsp,tcp,Revenue,Rent,Expenditure,Gsp,profit,Mobile,created_at)
            VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            """,
            (P_id,p_name,p_cat,qua,usp,ucp,tsp,tcp,tsp,rent,exp,gsp,pro,ph,now))
        conn.commit()
        conn.close()
    st.success("Data inserted into Sales Successfully..")
def delete():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("Delete from Employee")
    cur.execute("Delete from Employee_Duplicate")
    conn.commit()
    conn.close()
def delete1():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("Delete from Sales")
    conn.commit()
    conn.close()