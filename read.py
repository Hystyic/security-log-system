import pandas as pd
import streamlit as st
from database import view_all_data,view_all_manager,view_all_visitor


def read(table):
    if table=='resident':
        result = view_all_data()
        # st.write(result)
        df = pd.DataFrame(result, columns=['resident_id','Fname','Lname','Mob_no','block_id','house_id'])
        with st.expander("View all visitor"):
            st.dataframe(df)
    
    elif table=='security_manager':
        result = view_all_manager()
        # st.write(result)
        df = pd.DataFrame(result, columns=['manager_id','username','Fname','Lname','Mob_no','block_id','password','is_admin'])
        with st.expander("View all managers"):
            st.dataframe(df)
    elif table=='visitor':
        result = view_all_visitor()
        # st.write(result)
        df = pd.DataFrame(result, columns=['visitor_id','in_time','out_time','name','resident_id'])
        with st.expander("View visitors"):
            st.dataframe(df)