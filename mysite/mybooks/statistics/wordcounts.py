import datetime
from mybooks.models import Book


# words remaining until goal is reached:
def words_remaining(wordcount, goalwordcount):
    remaining = abs(goalwordcount-wordcount)
    return remaining # make this returnable in views

# words written since last time:
def words_added(wordcount, new_words):
    if wordcount and new_words:
        wordcount += new_words
    return wordcount # make this returnable in views

# words edited out since last time:
def words_deleted(wordcount, edited_out):
    if wordcount and edited_out:
        wordcount -= edited_out
    return wordcount # make this returnable in views


# avg words written per day:
def words_per_day(wordcount, goalwordcount):
    pass # make this returnable in views

    # use Pandas to find average per day!

    """pseudocode:

    for word in words:




    """
