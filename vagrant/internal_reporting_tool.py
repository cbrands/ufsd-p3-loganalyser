#! /usr/bin/env python3

"""
internal_reporting_tool is a tool to create reports out of a news database.
It runs three queries to answer these questions:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?
"""

import db_manager
import datetime

DB_NAME = "news"


if __name__ == '__main__':
    """
    Main function.
    Instantiates DbManager, runs the three queries and
    prints a report to the screen
    """
    print("Executing queries, please be patient")
    print(" ")
    db = db_manager.DbManager(DB_NAME)

    results = db.get_query_results("select * from popular_article_view limit 3")  # noqa
    print("1. What are the most popular three articles of all time?")
    for result in results:
        print("\t" + str(result[0]) + " - " + str(result[1]) + " views")
    print(" ")

    results = db.get_query_results("select * from popular_authors_view")
    print("2. Who are the most popular article authors of all time?")
    for result in results:
        print("\t" + str(result[0]) + " - " + str(result[1]) + " views")
    print(" ")

    results = db.get_query_results("select date, percent_error from error_log_view")  # noqa
    print("3. On which days did more than 1% of requests lead to errors?")
    for result in results:
        s = datetime.datetime.strptime(str(result[0]), "%Y-%m-%d")
        print("\t" + s.strftime("%d %B %Y") + " - " + str("{0:.2f}".format(result[1])) + " %")  # noqa
    print(" ")
