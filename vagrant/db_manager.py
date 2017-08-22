#! /usr/bin/env python3

import psycopg2


class DbManager():
    """
    This class manages the database connection and runs queries
    """
    def __init__(self, db_name):
        """
        Initializes DbManager
        db_name: The name of the database
        """
        self.db_name = db_name

    def connect(self, database_name="news"):
        """Connects to the database and returns a database connection."""
        try:
            db = psycopg2.connect(database=self.db_name)
            c = db.cursor()
            return db, c
        except psycopg2.Error:
            print ("Error connecting to the database")
            exit(1)

    def get_query_results(self, query):
        """Open connection, execute query, and return the results"""
        db, c = self.connect()
        c.execute(query)
        results = c.fetchall()
        db.close()
        return results
