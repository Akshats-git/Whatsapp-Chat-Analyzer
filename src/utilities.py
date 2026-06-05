from urlextract import URLExtract
import matplotlib.pyplot as plt
from wordcloud import WordCloud

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

    temp = df[df['message'] != '<Media omitted>\n']
    temp = temp[temp['message'] != 'This message was deleted\n']

    wc = WordCloud(width=400, height=400, min_font_size=10, background_color='white')
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))

    return df_wc

