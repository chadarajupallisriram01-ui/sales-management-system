import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),"..")))

import streamlit as st
from Database import get_connection
import pandas as pd
import streamlit.components.v1 as components




def Dashboard():
    st.title("Dashboard")
    st.markdown("""<p style="color:yellow">Click on Radio Buttons on side-panel""",unsafe_allow_html=True)
    conn = get_connection()
    cur = conn.cursor()
    emp_count = cur.execute("select count(*) from Employee").fetchone()[0]
    prod_count = cur.execute("select count(Distinct Product_Name) from Sales ").fetchone()[0]
    sales_count = cur.execute("select count(*) from Sales").fetchone()[0]

    st.subheader("Sales -> Automated KPIs")
    card_color = st.color_picker("you picked color","#60D9DC")
    def card(title,value,card_id):
        components.html(f'''
        <div style="background-color:{card_color};
            padding:20px;
            border-radius:20px;
            font-size:20px;
            font-weight:bold;
            text-align:left;
            box-shadow:0px 4px 10px rgba(0,0,0,0.5);
            cursor:pointer;
            color:white;
            transition:0.5s;">
            <h5>{title}</h5>
            <h1 id = "{card_id}" style="font-size:40px; margin:0;">0</h1>
        </div>
        <script>
            let count{card_id} = 0;
            let target{card_id} = {value};
            let speed{card_id} = 20;

            let update{card_id} = ()=>{{
                if(count{card_id} < target{card_id}){{
                    count{card_id}++;
                    document.getElementById("{card_id}").innerText = count{card_id};
                    setTimeout(update{card_id},speed{card_id});
                }}
            }}
            update{card_id}();
        </script>
        ''',height = 200)
    col1,col2,col3 = st.columns(3)
    with col1:
        card("Total Employees",emp_count,"emp")
    with col2:
        card("Total Products",prod_count,"prod")
    with col3:
        card("Total Sales",sales_count,"sal")

    st.divider()
    st.subheader("Line Chart -> Products Sold in Dates")
    query = "select created_at,count(*) as total_sales from Sales group by created_at order by created_at Desc"
    Sales_df = pd.read_sql_query(query,conn)
    st.line_chart(Sales_df.set_index("created_at"))

    st.divider()
    st.subheader("Recent Sales Records")
    n = st.number_input("Enter How many Sales done in recenly",1,step=1)
    query = "Select * from Sales order by Product_id Desc limit ?"
    df = pd.read_sql_query(query,conn,params=(n,))
    st.dataframe(df,column_order=["Sale_id","Product_id","Product_Name","Product_Category","Quntity","Usp","Ucp","Tsp","Tcp","Revenue","Rent","Expenditure","Gsp","Profit","Mobile"])
    

    st.divider()
    st.subheader("Bar Chart -> Sales on Products")
    query = "select Product_Name,count(*) as Total_Sales from Sales group by Product_Name order by Product_Name Desc"
    prod_df = pd.read_sql_query(query,conn)
    st.bar_chart(prod_df.set_index("Product_Name"))
    conn.close()
def emp_act():
    conn = get_connection()
    st.title("Employee Preformance")
    st.subheader("Employee Mobile numbers are here.")
    cur = conn.cursor()
    cur.execute("Select Distinct Mobile from Sales")
    f2 = cur.fetchall()
    df = pd.DataFrame(f2)
    st.write(df.T)
    mobile = st.text_input("Enter Mobile number : ",key ="mob11")
    st.button("Search")
    cur.execute("select * from Sales where Mobile= ?",(mobile,))
    f=cur.fetchall()
    if f:
        df = pd.DataFrame(f)
        st.write(df)
        st.divider()
        st.subheader("Employee Activity on Product_soldout and Profits")
        cur.execute("Select Profit,Product_Name from Sales where Mobile = ? group by Product_Name order by Profit Desc",(mobile,))
        f1 = cur.fetchall()
        prod_l = pd.DataFrame(f1,columns = ["Profit","Product_Name"])
        st.line_chart(prod_l.set_index("Product_Name"))
        st.divider()
        cur.execute("Select E.Name,sum(S.Profit) as Total_Profit , count(*) as Total_sales from Sales S inner join Employee E on E.Mobile = S.Mobile where S.Mobile = ?",(mobile,))
        f3 = cur.fetchall()
        df1 = pd.DataFrame(f3,columns = ["Name","Total_Profit","Total_Sales"])
        st.write(df1.T)
    else:
        if (not mobile.strip() == "") or (mobile !=i for i in f[0]):
            st.warning("Data not Found..")
            
    
