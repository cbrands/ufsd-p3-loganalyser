#! /usr/bin/env python3

"""
internal_reporting_tool is a tool to create reports out of a news database.
"""

import db_manager

DB_NAME = "news"



#def connect(database_name="news"):
#    """Connects to the database and returns a database connection."""
#    try:
#        db = psycopg2.connect(database=DB_NAME)
#        c = db.cursor()
#        return db, c
#    except psycopg2.Error:
#        print ("Error connecting to the database")
#        exit(1)
#
#
#def get_query_results(query):
#    """Open connection, execute query, and return the results"""
#    db, c = connect()
#    c.execute(query)
#    results = c.fetchall()
#    db.close()
#    return results



if __name__=='__main__':
    print("testing query3")
    #results = get_query_results("select * from popular_article_view limit 3")
    #results = get_query_results("select * from popular_authors_view")
    db = db_manager.DbManager(DB_NAME)
    results = db.get_query_results("select date, percent_error from error_log_view")
    for result in results:
        print(result)
