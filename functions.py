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