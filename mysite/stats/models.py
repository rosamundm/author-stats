from mybooks.models import Book
from users.models import CustomUser
from datetime import datetime, timezone, tzinfo
from simple_history.models import HistoricalRecords


class BookStat(Book):
    def __init___(self):
        super().__init___()

        book = Book.objects.get(id=id)

        last_login = book.history.last().last_login

        # active_users = CustomUser.objects.filter(last_login__lte=now)

        now = datetime.datetime.now()

        if last_login < now:
            wordcount_at_last_login = book.history.as_of(last_login)
            wordcount_now = self.wordcount

        def words_added(self):
            """
            find out how many words were added since last session
            """
            # user sessions?
            # 1. get last_login
            # 2. make as_of query with last_login as lookup

            if wordcount_at_last_login < wordcount_now:
                difference = abs(wordcount_now - wordcount_at_last_login)
                new_wordcount = wordcount_now + difference
                return new_wordcount

        def words_deleted(self):
            """
            find out how many words were deleted since last session
            """

            if wordcount_at_last_login > wordcount_now:
                deleted_words = abs(wordcount_at_last_login - wordcount_now)
                return deleted_words
