#! /usr/bin/env python3

"""
internal_reporting_tool is a tool to create reports out of a news database.
"""

#import PostgreSQL driver
import psycopg2

DB_NAME = "news"

def connect(database_name="news"):
    """Connects to the database and returns a database connection."""
    try:
        db = psycopg2.connect(database=DB_NAME)
        c = db.cursor()
        return db, c
    except psycopg2.Error:
        print ("Error connecting to the database")
        exit(1)


def get_query_results(query):
    """Open connection, execute query, and return the results"""
    db, c = connect()
    c.execute(query)
    results = c.fetchall()
    db.close()
    return results

if __name__=='__main__':
    print("testing database connection and get_query_results")
    results = get_query_results("select * from articles limit 10")
    for result in results:
        print(result)
