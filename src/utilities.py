from urlextract import URLExtract

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

