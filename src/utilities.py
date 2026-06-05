
def fetch_stats(selected_user, df):
    if selected_user == "Group":
        num_messages = df.shape[0]
    else:
        num_messages = df[df['user'] == selected_user].shape[0]
    return num_messages