# Team-14-Predict
A group project on python functions
These functions give us insight about Eskom.
These functions all use Eskom data/variables

## Function 1: Metric Dictionary 
This function takes in data and returns sample statistics such as the mean, median, standard deviation, variance as well as the min
and max values.

## Function 2: Five Number Summary
This function takes n data and returns the five number summary as a dictionary.

## Function 3: Date Parser
This function takes as input a list of these datetime strings and returns only the date in 'yyyy-mm-dd' format.

## Function 4: Municipality and Hashtag Detector
This function takes in a pandas dataframe and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet.

## Function 5: Number of tweets per day
This function calculates the number of tweets that were posted per day.

## Function 6: Word Splitter
This function splits the sentences in a dataframe's column into a list of the separate words. The created lists should be placed in a column named 'Split Tweets' in the original dataframe.

## Function 7: Stop Words
 This function removes english stop words from a tweet.

# grouppackage
This package consists of functions used to extract values from a dataframe such as dates, number of tweets 
municipalities where these tweets were directed to. This package also does some descriptive analysis
of certain values per Province eg mean, median, variance

## build package locally
'python setup.py sdist'

## installing package from github
'pip install git+https://github.com/Confidono/Team-14-Predict.git'
## updating package from github
'pip install --upgrade git+https://github.com/Confidono/Team-14-Predict.git'
## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## A thank you to all the contributors
Iman Mokwena 
Valaska
Primrose
Lebo
Thando

## License
[MIT](https://choosealicense.com/licenses/mit/)
