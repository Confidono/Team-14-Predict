import unittest
import groupModule

class TestFuncs(unittest.TestCase):
    '''
    Testing dictionary_of_metrics function
    '''
    def test_dictionary_of_metrics(self):
        self.assertEqual(groupModule.dictionary_of_metrics([39660, 36024, 32127, 39488, 18422]), {'mean':33144.2 , 'median': 36024.0, 'var': 77192641.2, 'std': 8785.93, 'min': 18422, 'max': 39660})
        self.assertEqual(groupModule.dictionary_of_metrics([51860, 68121, 49881, 42034, 54646]), {'mean': 53308.4, 'median': 51860.0, 'var': 90539830.3, 'std': 9515.24, 'min': 42034, 'max': 68121})

    def test_five_num_summary(self):
        self.assertEqual(groupModule.five_num_summary([39660, 36024, 32127, 39488, 18422]), {'max': 39660, 'median': 36024.0, 'min': 18422, 'q1': 32127.0, 'q3': 39488.0})
        self.assertEqual(groupModule.five_num_summary([51860, 68121, 49881, 42034, 54646]), {'max': 68121, 'median': 51860.0, 'min': 42034, 'q1': 49881.0, 'q3': 54646.0})
   
    def test_date_parser(self):
        self.assertEqual(groupModule.date_parser(['2019-11-29 12:50:54','2019-11-29 12:46:53','2019-11-29 12:46:10']),['2019-11-29', '2019-11-29', '2019-11-29'] )
        self.assertEqual(groupModule.date_parser(['2020-11-29 12:50:54','2019-11-20 12:46:53','2007-07-07 12:46:10']), ['2020-11-29','2019-11-20','2007-07-07'])

if __name__ == '__main__':
    unittest.main()