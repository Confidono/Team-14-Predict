import numpy as np
import pandas as pd

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

def date_parser(dates):
    """This function takes a list of strings with date and time then
    it returns a string with only the date
    """
    new_dates = []
    for i in range(len(dates)):
        a = dates[i][:10]        
        new_dates.append(a)
    return new_dates