
import os
import sqlite3

dirname = os.path.dirname(__file__)


def get_database_connection():
    connection = sqlite3.connect(os.path.join(
        dirname, "../..", "data", "database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection


def get_fake_database_connection():
    connection = sqlite3.connect(os.path.join(
        dirname, "../..", "data", "fake_database.sqlite"))
    connection.row_factory = sqlite3.Row
    return connection
