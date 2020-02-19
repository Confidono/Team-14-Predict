import numpy as np
import pandas as pd
import datetime as datetime

#Function 1
def dictionary_of_metrics(items):
    """This function calculates the mean, median, variance,standard deviation, min and max
    of a list argument and returns a dictionary of the results

    Example:
    list of numbers 

    Returns:

    dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}
    """
    np_list = np.array(items) #create an array of list to use numpy functions on list
    metric_dict = {'mean': np.mean(np_list).round(2),
                   'median': np.median(np_list).round(2),
                   'var': np.var(np_list, ddof=1).round(2),
                   'std': np.std(np_list, ddof=1).round(2),
                   'min': np.min(np_list).round(2),
                   'max': np.max(np_list).round(2),} #create a dictionary that calculates the five metrics
 
    return metric_dict #return result as a dictionary

#Function 2
def five_num_summary(items):
    """This function takes in a list of integers and returns a dictionary of the five number summary"""
    np_list = np.array(items)
    metric_dict = {'max': np.max(np_list).round(2),
                   'median': round(np.median(np_list), 2),
                   'min': np.min(np_list).round(2),
                   'q1': np.quantile(np_list, 0.25).round(2),
                   'q3': np.quantile(np_list, 0.75).round(2),
                   }
    
    return metric_dict

#Function 3
def date_parser(dates):
    """This function takes a list of strings with date and time then
    it returns a string with only the date
    """
    new_dates = []
    for i in range(len(dates)):
        a = dates[i][:10]        
        new_dates.append(a)
    return new_dates

#Function 4
def extract_municipality_hashtags(df):
    """
         takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information
         about the municipality and hashtag of the tweet.
        Params:
            df: A pandas dataframe
        Returns:
            df: A modified dataframe
    """
    municipality = []
    hashtags = []                    #creates two empty lists

    tweets = [i.split(" ") for i in df['Tweets']]   #creates a list from datframe column

    new_munic_list = []
    new_tag_list = []           #final set of lists that will be added into the dataframe

    for tweet in tweets: # appends the initial set of lists to extract words starting with # and key values of mun dict
        municipality.append([mun_dict[word] for word in tweet if word in list(mun_dict.keys())])
        hashtags.append([tag.lower() for tag in tweet if tag.startswith('#')])

    for item in municipality:
        if item == []: 
            item = np.nan    #if list is empty, retunr NaN
        new_munic_list.append(item)

    for tag in hashtags:
        if tag == []:
            tag = np.nan
        new_tag_list.append(tag)
    
    df['municipality'] = new_munic_list  #creates two new columns in dataframe with #'s and key values from mun_dict dictionary
    df['hashtags'] = new_tag_list
  
    return df

#Function 5
def number_of_tweets_per_day(df):
     """
        calculates the number of tweets that were posted per day.
        Params:
            df: A dataframe of tweets.
        Return:
            df: A dataframe with the tweet-count per day.
    """
    
    var_date = pd.to_datetime(df['Date']) #creates a datetime variable from dates column
    df['Date'] = [i.date() for i in var_date]  
    by_date = df.groupby('Date').count() #groups dataframe by date and counts number of tweets
    
    return by_date

#Function 6
    
def word_splitter(df):
    """
        Splits the sentences in a dataframe's column into a list of the separate words.

        Params:
            df: A pandas dataframe.

        Returns:
            df: The pandas dataframe with an extra column of split tweets.
    """
    df['Split Tweets'] = [i.lower().split() for i in df['Tweets']]
    return df

#Function 7
def stop_words_remover(df):
   """
        Removes english stop words from a tweet.
        Params:
            df: A pandas dataframe.
        Returns:
            df: Modified dataframe
    """
    #applying lambda expression mapping the stop words values in the stop words dictionary with any stop wods existing in Tweets
    df['Without Stop Words'] = df['Tweets'].apply(lambda x: [item for item in str(x).lower().split() if item not in stop_words_dict['stopwords']])

    return df


