import datetime
from mybooks.models import Book


# words remaining until goal is reached:
def words_remaining(wordcount, goalwordcount):
    remaining = abs(goalwordcount-wordcount)
    return remaining

# words written since last time:
def words_added(wordcount, x):
    count = wordcount
    x = new_words
    wordcount += new_words
    return wordcount


# words edited out since last time:
def words_deleted(wordcount, goalwordcount):
    pass


# avg words written per day:
def words_per_day(wordcount, goalwordcount):
    pass
