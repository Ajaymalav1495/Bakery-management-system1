
import streamlit as st
import mysql.connector
import pandas as pd


def employee_page():
    st.title("Employee Page")
    st.write("----")
    class employee1:
        def check_inputs(input2, input3):
            results = []
            for i, input_string in enumerate([input2, input3], start=1):
                if input_string.strip() == "":
                    results.append(f"Input {i} is empty")
                else:
                    results.append(f"Input {i} is not empty")
            return results

        def all_inputs_not_empty(input2, input3):
            return all(input_string.strip() != "" for input_string in [input2, input3])

        # Streamlit inputs
        emp_name = st.text_input("Enter Employee Name:")
        salary = st.text_input("Enter Salary:")

        # Check inputs and display results
        if st.button("Submit"):
            input2 = emp_name
            input3 = salary

            results = check_inputs(input2, input3)
            for result in results:
                st.write(result)

            if all_inputs_not_empty(input2, input3):
                try:
                    # Establish database connection
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",  
                        database="bakery"
                    )
                    c = conn.cursor()

                    # Insert query
                    query = "INSERT INTO employee (Employee_name, Salary) VALUES (%s, %s)"
                    c.execute(query, (emp_name, salary))

                    # Commit changes
                    conn.commit()
                    st.success("Data inserted successfully!")
                except mysql.connector.Error as e:
                    st.error(f"Error: {e}")
                finally:
                    # Close the connection
                    conn.close()
            else:
                st.error("Sorry, all fields must be filled.")
    st.write("---")

    #search 
    st.markdown("Search Box  :")
    class employee2:
        a = st.text_input("Enter employee ID :")
        if st.button("Search"):
            try:
                conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="bakery"
                    )
                c = conn.cursor()
                query = "SELECT * FROM employee where employee_ID  in(%s)"
                c.execute(query,(a,))
                data = c.fetchall()
                df = pd.DataFrame(data, columns=['Employee_id', 'Employee_name', 'Salary','Attendance'])
                st.dataframe(df)
            except mysql.connector.Error as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()
        st.write("----")
        # Show all records
        if st.button("Show"):
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="bakery"
                )
                c = conn.cursor()
                query = "SELECT * FROM employee"
                c.execute(query)
                data = c.fetchall()
                df = pd.DataFrame(data, columns=['Employee_id', 'Employee_name', 'Salary','Attendance'])
                st.dataframe(df)
            except mysql.connector.Error as e:
                st.error(f"Error: {e}")
            finally:
                conn.close()
    st.write("---")
