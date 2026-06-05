import streamlit as st
from src.preprocess import preprocess_chat
from src import utilities

st.sidebar.title("Whatsapp Chat Analyzer")

uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()

    # Decode the bytes data to a string
    data = bytes_data.decode("utf-8")

    df = preprocess_chat(data)
    st.dataframe(df)

    # fetching unique users and sorting them
    user_list = df['user'].unique().tolist()
    if 'group_notification' in user_list:   
        user_list.remove('group_notification')
    user_list.sort()
    user_list.insert(0,"Group")

    selected_user = st.sidebar.selectbox("Select User for Analysis: ", user_list)

    if st.sidebar.button("Show Analysis"):

        num_messages = utilities.fetch_stats(selected_user, df)
        
        col1, col2, col3, col4 = st.columns(4)

        # Displaying the total number of messages in the first column
        with col1:
            st.header("Total Messages")
            st.title(num_messages)