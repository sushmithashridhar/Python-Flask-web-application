from abc import ABC, abstractmethod

class IModel(ABC):
    """
    This is a class for Model.

    Attributes:
    data (text): The data inserted to the sqlite3 database.
    """
    @abstractmethod
    def fetchall(self, data):
        pass
    """
    This is a fetchall function to fetch all the data inserted to sqlite3 database.

    :param data: The data inserted to the sqlite3 database.
    :returns: returns the data
    """
