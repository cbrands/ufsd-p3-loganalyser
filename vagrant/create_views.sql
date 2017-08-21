create or replace view popular_article_view as select title, count(*) as views from articles, log where log.path like concat('%',articles.slug) group by title order by views desc;

create or replace view popular_authors_view as select authors.name, count(*) as views from articles, log, authors where log.path like concat('%',articles.slug) and articles.author = authors.id group by authors.name order by views desc;

create or replace view error_log_view as select date,total,error, (error::float * 100.0) / total::float as percent_error from
(select date(time) as date, count(status) as total,
sum(case status when '200 OK' then 0 else 1 end) as error from log
group by date(time)) as result
where (error::float * 100.0) / total::float > 1.0 order by percent_error desc;