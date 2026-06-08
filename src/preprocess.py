import re
import pandas as pd

def preprocess_chat(chat):
    pattern = r'\d{1,2}/\d{1,2}/\d{2,4},\s\d{1,2}:\d{2}(?:\s?[ap]m)?\s-\s'

    # Removing the empty and custom system messages
    messages = re.split(pattern, chat)[4:]   
    dates = re.findall(pattern, chat)[3:]    

    df = pd.DataFrame({'user_message': messages, 'date': dates})

    # Converting the date column to datetime format
    df['date'] = pd.to_datetime(        
        df['date'],
        format='%d/%m/%y, %I:%M %p - '
    )

    #seperate users and messages
    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])

    df['user'] = users
    df['message'] = messages
    df.drop(columns=['user_message'], inplace=True)

    # Extracting year, month, day, hour, and minute from the date column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['only_date'] = df['date'].dt.date
    df['day'] = df['date'].dt.day
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute
    df['day_name'] = df['date'].dt.day_name()

    return df
