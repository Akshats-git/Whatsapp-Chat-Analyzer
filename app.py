import streamlit as st
from src.preprocess import preprocess_chat
from src import utilities
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

st.set_page_config(
    page_title="WhatsApp Chat Analyzer",
    page_icon="",
    layout="wide"
)

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

        # Fetching the stats    
        st.header("Top Statistics")
        num_messages, num_words, num_media_messages, num_links = utilities.fetch_stats(selected_user, df)
        col1, col2, col3, col4 = st.columns(4)

        # Displaying the total number of messages in the first column
        with col1:
            st.header("Total Messages")
            st.title(num_messages)

        # Displaying the total number of words in the second column
        with col2:
            st.header("Total Words")
            st.title(num_words)

        # Displaying the total number of media messages in the third column
        with col3:
            st.header("Total Media Messages")
            st.title(num_media_messages)

        # Displaying the total number of links shared in the fourth column
        with col4:
            st.header("Total Links Shared")
            st.title(num_links)

        # Monthly Timeline
        st.title("Monthly Timeline")
        timeline = utilities.monthly_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(timeline['time'], timeline['message'], color='green')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Daily Timeline
        st.title("Daily Timeline")
        daily_timeline = utilities.daily_timeline(selected_user, df)
        fig, ax = plt.subplots()
        ax.plot(daily_timeline['only_date'], daily_timeline['message'], color='black')
        plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Activity Map
        st.title("Activity Map")
        col1, col2 = st.columns(2)

        with col1:
            st.header("Weekly")
            busy_day = utilities.weekly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_day.index, busy_day.values, color='orange')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)
        
        with col2:
            st.header("Monthly")
            busy_month = utilities.monthly_activity_map(selected_user, df)
            fig, ax = plt.subplots()
            ax.bar(busy_month.index, busy_month.values, color='purple')
            plt.xticks(rotation='vertical')
            st.pyplot(fig)

        # User Activity Heatmap
        st.title("User Activity Heatmap")
        user_heatmap = utilities.activity_heatmap(selected_user, df)
        fig, ax = plt.subplots()
        sns.heatmap(user_heatmap, cmap='YlGnBu')
        ax.set_xlabel("Hour of Day")
        ax.set_ylabel("Day of Week")
        st.pyplot(fig)

        # Finding the most active users in a group
        if selected_user == "Group":
            st.title("Most Active Users")
            x, new_df = utilities.most_busy_users(df)
            fig, ax = plt.subplots()
            col1, col2 = st.columns(2)

            with col1:
                ax.bar(x.index, x.values, color='lightgreen')
                plt.xticks(rotation='vertical')
                st.pyplot(fig)

            with col2:
                st.dataframe(new_df)

        # Wordcloud
        st.title("Wordcloud")   
        df_wc = utilities.create_wordcloud(selected_user, df)
        fig, ax = plt.subplots()
        ax.imshow(df_wc)
        st.pyplot(fig)

        # Most common words
        st.title("Most Common Words")
        most_common_df = utilities.most_common_words(selected_user, df)
        fig, ax = plt.subplots()
        ax.barh(most_common_df[0], most_common_df[1], color='pink')
        # plt.xticks(rotation='vertical')
        st.pyplot(fig)

        # Emoji Analysis
        st.title("Emoji Analysis")
        emoji_df = utilities.emoji_stats(selected_user, df)
        col1, col2 = st.columns(2)

        with col1:
            st.dataframe(emoji_df)
        with col2:
            fig = px.pie(
                emoji_df.head(10),
                values='count',
                names='emoji',
                title='Top Emojis'
            )
            st.plotly_chart(fig, width='stretch')

        

            