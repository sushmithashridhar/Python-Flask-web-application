from IModel import IModel
import sqlite3
DB_FILE = 'entries.db'



class AppModel(IModel):

    """
    This is a class for Model.

    Attributes:
    data (text): The data inserted to the sqlite3 database.
    """
    if __name__ == '__main__':
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(rowid) from reviews")
            print('working')
        except sqlite3.OperationalError:
            cursor.execute(
                "create table reviews (termoffered text, yearoffered text, timeoftheweekoffered text, instructor text, review text, rating text)")
        cursor.close()

    def fetchall(self, data):
        return 'Review'
    """
    This is a fetchall function to fecth all the data inserted to sqlite3 database.

    :param data: The data inserted to the sqlite3 database.
    :returns: returns the data
    """


    def select(self):

        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM reviews")
        return cursor.fetchall()
    """
    This is a select function to select all the data from the table reviews of sqlite3 database.

    :param: No parameter passed.
    :returns: returns the data retrieved from select query
    """

    def insert(self, data):

        params = {'termoffered': data['termoffered'], 'yearoffered': data['yearoffered'], 'timeoftheweekoffered': data['timeoftheweekoffered'], 'instructor': data['instructor'], 'review': data['review'], 'rating': data['rating']}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO reviews(termoffered, yearoffered, timeoftheweekoffered, instructor, review, rating) VALUES (:termoffered, :yearoffered, :timeoftheweekoffered, :instructor, :review, :rating)", params)
        connection.commit()
        cursor.close()
        return 'true'
    """
    This is a insert function to insert the data to the table reviews of sqlite3 database.

    :param: No parameter passed.
    :returns: returns the data retrieved from select query
    """

