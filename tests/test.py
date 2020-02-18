import groupModule

def test_dictionary_of_metrics():
    '''
    Make sure dictionary_of_metrics works correctly
    '''
    assert groupModule.dictionary_of_metrics([39660, 36024, 32127, 39488, 18422]) ==  {'mean': 33144.2, 'median': 36024.0, 'var': 77192641.2, 'std': 8785.93, 'min': 18422, 'max': 39660} , 'incorrect'