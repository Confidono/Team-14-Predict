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
