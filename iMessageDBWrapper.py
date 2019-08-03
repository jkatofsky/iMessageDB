import sqlite3
import pandas
from data_clean import *

# https://towardsdatascience.com/heres-how-you-can-access-your-entire-imessage-history-on-your-mac-f8878276c6e9
# https://github.com/yortos/imessage-analysis/blob/master/imessages-data-extract-and-prep.ipynb


class iMessageDBWrapper(object):

    def __init__(self, path_to_db="~/Library/Messages/chat.db"):
        self.conn = sqlite3.connect(path_to_db)

    def get_handle_metadata(self):
        return clean_handle_df(pandas.read_sql_query("SELECT * FROM handle", self.conn))

    def get_chat_metadata(self):
        return clean_chat_df(pandas.read_sql_query("SELECT * FROM chat", self.conn))

    def query_with_custom_conditions(self, conditions):
        if not conditions:
            return
        return clean_message_df(pandas.read_sql_query("SELECT * FROM message WHERE %s" % conditions, self.conn))

    def get_all_messages(self, handle_id=None, chat_id=None):
        if handle_id and chat_id:
            df = pandas.read_sql_query("SELECT * FROM message WHERE handle_id == %s AND chat_id == %s"
                                       % (handle_id, chat_id), self.conn)
        elif handle_id:
            df = pandas.read_sql_query("SELECT * FROM message WHERE handle_id == %s"
                                       % (handle_id), self.conn)
        elif chat_id:
            df = pandas.read_sql_query("SELECT * FROM message WHERE chat_id == %s"
                                       % (chat_id), self.conn)
        else:
            df = pandas.read_sql_query("SELECT * FROM message", self.conn)

        return clean_message_df(df)

    def get_messages_random(self, amount, handle_id=None, chat_id=None):

        if handle_id and chat_id:

            where_clause = "handle_id == %s AND chat_id == %s" % (handle_id, chat_id)

            df = pandas.read_sql_query("SELECT * FROM message\
                WHERE %s AND ROWID IN (SELECT ROWID FROM message\
                    WHERE %s ORDER BY RANDOM() LIMIT %i)" % (where_clause, where_clause, amount), self.conn)

        elif handle_id:

            where_clause = "handle_id == %s" % (handle_id)

            df = pandas.read_sql_query("SELECT * FROM message\
                WHERE %s AND ROWID IN (SELECT ROWID FROM message\
                    WHERE %s ORDER BY RANDOM() LIMIT %i)" % (where_clause, where_clause, amount), self.conn)
        elif chat_id:
            where_clause = "chat_id == %s" % (chat_id)

            df = pandas.read_sql_query("SELECT * FROM message\
                WHERE %s AND ROWID IN (SELECT ROWID FROM message\
                    WHERE %s ORDER BY RANDOM() LIMIT %i)" % (where_clause, where_clause, amount), self.conn)
        else:
            df = pandas.read_sql_query("SELECT * FROM message\
                WHERE ROWID IN (SELECT ROWID FROM message ORDER BY RANDOM() LIMIT %i)" % (amount), self.conn)

        return clean_message_df(df)
