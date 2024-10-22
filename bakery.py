import streamlit as st


# Import your page files
from Home import home_page
from Employee import employee_page
from Customer import customer_page
from Inventory import inventory_page
from Billing import billing_page

# Create a sidebar menu
with st.sidebar:
        menu_title = "Main Menu"
        options = ["Home", "Employee", "Customer", "Inventory", "Billing"]
        selected = st.selectbox(menu_title, options)
    
# Redirect to the selected page
if selected == "Home":
    home_page()
elif selected == "Employee":
    employee_page()
elif selected == "Customer":
    customer_page()
elif selected == "Inventory":
    inventory_page()
elif selected == "Billing":
    billing_page()
