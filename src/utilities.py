from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter
import pandas as pd
import emoji

def fetch_stats(selected_user, df):

    if selected_user != "Group":
        df = df[df['user'] == selected_user]

    # Getting the total number of messages
    num_messages = df.shape[0]

    # Getting the total number of words
    words = []
    for message in df['message']:
        words.extend(message.split())
    num_words = len(words)

    # Getting the total number of media messages
    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    # Getting the total number of links shared
    extractor = URLExtract()
    links = []
    for message in df['message']:
        links.extend(extractor.find_urls(message))
    num_links = len(links)

    return num_messages, num_words, num_media_messages, num_links


def most_busy_users(df):
    # Fetching the most active users in a group
    x = df['user'].value_counts().head()

    # Fetching the percentage of messages sent by each user
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})

    return x, df


def create_wordcloud(selected_user, df):

    if selected_user != "Group":
        df = df[df['user'] == selected_user]

    f = open('data/stop_words.txt', 'r')
    stop_words = f.read()

    # Removing certain system messages
    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']
    temp = temp[temp['message'] != 'group_notification']

    # Removing emojis from the messages
    temp['message'] = temp['message'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))

    # Filtering out the stop words from the messages and finding the most common words
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    wc = WordCloud(width=400, height=400, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc


def most_common_words(selected_user, df):

    f = open('data/stop_words.txt', 'r')
    stop_words = f.read()

    if selected_user != "Group":
        df = df[df['user'] == selected_user]

    # Removing certain system messages
    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']
    temp = temp[temp['message'] != 'group_notification']

    # Removing emojis from the messages
    temp['message'] = temp['message'].apply(lambda x: x.encode('ascii', 'ignore').decode('ascii'))

    # Filtering out the stop words from the messages and finding the most common words
    words = []
    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df


def emoji_stats(selected_user, df):

    if selected_user != "Group":
        df = df[df['user'] == selected_user]

    emojis = []

    # Extracting emojis from the messages
    for message in df['message']:
        emoji_list = emoji.emoji_list(str(message))

        for item in emoji_list:
            emojis.append(item['emoji'])

    emoji_df = pd.DataFrame(
        Counter(emojis).most_common(),
        columns=['emoji', 'count']
    )

    return emoji_df

