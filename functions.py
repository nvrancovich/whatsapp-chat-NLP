import pandas as pd
import re

def n_messages_time(df):
    df = df[['date', 'message']]
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.groupby(['year', 'month']).count()['message']
    return df

def n_words_time(df, words, start_date, end_date):
    
    mask = (df['date'] > start_date) & (df['date'] <= end_date)
    df = df.loc[mask]
    
    if len(words) == 1:
        mask = df['message'].str.contains(words[0])
        df = df.loc[mask]
        
    if len(words) == 2:
        mask = (df['message'].str.contains(words[0]) |
                df['message'].str.contains(words[1]))
        df = df.loc[mask]
        
    if len(words) == 3:
        mask = (df['message'].str.contains(words[0]) |
                df['message'].str.contains(words[1]) |
                df['message'].str.contains(words[2]))
        df = df.loc[mask]
        
    if len(words) == 4:
        mask = (df['message'].str.contains(words[0]) |
                df['message'].str.contains(words[1]) |
                df['message'].str.contains(words[2]) |
                df['message'].str.contains(words[3]))
        df = df.loc[mask]
        
    if len(words) == 5:
        mask = (df['message'].str.contains(words[0]) |
                df['message'].str.contains(words[1]) |
                df['message'].str.contains(words[2]) |
                df['message'].str.contains(words[3]) |
                df['message'].str.contains(words[4]))
        df = df.loc[mask]
    
    df = df.loc[mask]
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month
    df = df.groupby(['year', 'month']).count()['message']
    
    return df

def parse_file(text_file):
    '''Convert WhatsApp chat log text file to a Pandas dataframe.'''
    
    # some regex to account for messages taking up multiple lines
    pat = re.compile(r'^(\d\d\/\d\d\/\d\d\d\d.*?)(?=^^\d\d\/\d\d\/\d\d\d\d|\Z)', re.S | re.M)
    with open(text_file) as f:
        data = [m.group(1).strip().replace('\n', ' ') for m in pat.finditer(f.read())]

    sender = []; message = []; datetime = []
    for row in data:

        # timestamp is before the first dash
        datetime.append(row.split(' - ')[0])

        # sender is between am/pm, dash and colon
        try:
            s = re.search('m - (.*?):', row).group(1)
            sender.append(s)
        except:
            sender.append('')

        # message content is after the first colon
        try:
            message.append(row.split(': ', 1)[1])
        except:
            message.append('')

    df = pd.DataFrame(zip(datetime, sender, message), columns=['timestamp', 'sender', 'message'])
    df['timestamp'] = pd.to_datetime(df.timestamp, format='%d/%m/%Y, %I:%M %p')

    # remove events not associated with a sender
    df = df[df.sender != ''].reset_index(drop=True)
    
    return df