import pandas as pd
import streamlit as st
from database import view_all_data, view_only_resident_names, delete_data,view_all_manager,view_all_visitor,view_only_manager,delete_data_hostel_manager,view_only_visitor,delete_visitor


def delete(table):
    if table=='visitor':
        result = view_all_data()
        df = pd.DataFrame(result, columns=['resident_id','Fname','Lname','Mob_no','block_id','house_id'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_resident = [i[0] for i in view_only_resident_names()]
        selected_resident = st.selectbox("visitor to Delete", list_of_resident)
        st.warning("Do you want to delete ::{}".format(selected_resident))
        if st.button("Delete visitor"):
            delete_data(selected_resident)
            st.success("visitor has been deleted successfully")
        new_result = view_all_data()
        df2 = pd.DataFrame(new_result, columns=['resident_id','Fname','Lname','Mob_no','block_id','house_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)
    elif table=='security_manager':
        result = view_all_manager()
        df = pd.DataFrame(result, columns=['manager_id','username','Fname','Lname','Mob_no','block_id','password','is_admin'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_admin = [i[0] for i in view_only_manager()]
        selected_admin = st.selectbox("admin to Delete", list_of_admin)
        st.warning("Do you want to delete ::{}".format(selected_admin))
        if st.button("Delete warden"):
            delete_data_hostel_manager(selected_admin)
            st.success("warden has been deleted successfully")
        new_result = view_all_manager()
        df2 = pd.DataFrame(new_result, columns=['manager_id','username','Fname','Lname','Mob_no','block_id','password','is_admin'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='visitor':
        result = view_all_visitor()
        df = pd.DataFrame(result, columns=['Category','No_of_persons','Cost_per_day','LateFee_charges'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_visitor = [i[0] for i in view_only_visitor()]
        selected_visitor = st.selectbox("visitor to Delete", list_of_visitor)
        st.warning("Do you want to delete ::{}".format(selected_visitor))
        if st.button("Delete visitor"):
            delete_visitor(selected_visitor)
            st.success("visitor has been deleted successfully")
        new_result = view_all_visitor()
        df2 = pd.DataFrame(new_result, columns=['visitor_id','in_time','out_time','name','resident_id'])
        with st.expander("Updated data"):
            st.dataframe(df2)
