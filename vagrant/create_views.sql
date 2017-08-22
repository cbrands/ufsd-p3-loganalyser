-- This view is for answering the following question
-- 1. What are the most popular three articles of all time?
CREATE OR replace VIEW popular_article_view AS SELECT title, Count(*) AS views 
    FROM articles, log 
    WHERE log.path LIKE Concat('%',articles.slug) 
    GROUP BY title 
    ORDER BY views DESC;

-- This view is for answering the following question
-- 2. Who are the most popular article authors of all time?
CREATE OR replace VIEW popular_authors_view AS SELECT authors.NAME, Count(*) AS views 
    FROM articles, log, authors 
    WHERE log.path LIKE Concat('%',articles.slug) 
    AND articles.author = authors.id 
    GROUP BY authors.NAME 
    ORDER BY views DESC;

-- This view is for answering the following question
-- 3. On which days did more than 1% of requests lead to errors?
CREATE OR replace VIEW error_log_view AS SELECT date, total, error, 
         (error::float * 100.0) / total::float AS percent_error 
    FROM ( 
        SELECT date(time) AS date, 
        count(status) AS total, 
        sum( 
            CASE status 
                WHEN '200 OK' THEN 0 
                ELSE 1 
                END) AS error 
        FROM log 
        GROUP BY date(time)) AS result 
    WHERE (error::float * 100.0) / total::float > 1.0 
    ORDER BY percent_error DESC;