import datetime
from mybooks.models import Book


# words remaining until goal is reached:
def words_remaining(wordcount, goalwordcount):
    remaining = abs(goalwordcount-wordcount)
    return remaining

# words written since last time:
def words_added(wordcount, new_words):
    if wordcount and new_words:
        wordcount += new_words
    return wordcount

# words edited out since last time:
def words_deleted(wordcount, edited_out):
    if wordcount and edited_out:
        wordcount -= edited_out
    return wordcount


# avg words written per day:
def words_per_day(wordcount, goalwordcount):
    pass
