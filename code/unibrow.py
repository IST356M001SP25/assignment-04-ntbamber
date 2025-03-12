'''
Solution unibrow.py
'''
import pandas as pd
import streamlit as st
import pandaslib as pl

st.title("UniBrow")
st.caption("The Universal data browser")

file = st.file_uploader("Upload a file", type=["xlsx", "csv", "json"]) #file upload creation
if file is not None: #checks if file is uploaded
    ext = pl.get_file_extension(file.name) #uses pandaslib to fetch file extension
    df = pl.load_file(file, ext) #uses pandaslib to load file
    #df display
    st.write("Dataframe:") #title for df display
    st.dataframe(df) #displays df
    
    # column selection
    columns = st.multiselect("Select columns to display", pl.get_column_names(df), default=pl.get_column_names(df)) #uses multiselect and pandaslib get column names to select columns
    filtered_df = df[columns] #displays df with selected columns
    
    # filtering dataframe based on text column
    text_column = st.selectbox("Select a text column to filter", pl.get_columns_of_type(filtered_df, 'object')) #shows all numpy_type columns and allows for selection of one
    filter_value = st.text_input(f"Enter a value to filter {text_column} column") #text input box with name changing based on selected column
    
    if filter_value: #checks for entered filter value
        filtered_df = filtered_df[filtered_df[text_column].str.contains(filter_value, na=False)] #displays df rows that contain the filter value
    
    # filtered df display
    st.write("Filtered Dataframe:") #title for filtered df
    st.dataframe(filtered_df) #displays filtered df
    
    # desctriptive statistics df display
    st.write("Dataframe Statistics:") #title for df statistics
    st.write(filtered_df.describe()) #displays df statistics