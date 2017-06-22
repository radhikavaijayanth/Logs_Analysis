#! /usr/bin/env python3
import psycopg2
# Variable to store db name
Source_Name = "news"
# Question1 & it's answer
question_1 = "What are the three most popular articles of all time?"
query_1 = "select title,visit_count from info_view limit 3"

# Question2 & it's answer
question_2 = "Who are the most popular article authors of all time?"
query_2 = (
    "SELECT authors.name,sum(info_view.visit_count) as author_views from "
    "info_view,authors where authors.id = info_view.author "
    "group by authors.name order by author_views desc")

# Question3 & it's answer
question_3 = "On which days did more than 1% of requests lead to errors?"
query_3 = (
    "select day_val, perc_err from ("
    "select day_val, round((sum(request_err)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day_val) * 100), 2) as "
    "perc_err from (select substring(cast(log.time as text), 0, 11) as day_val, "
    "count(*) as request_err from log where status like '%404%' group by day_val)"
    "as perc_val group by day_val order by perc_err desc) as answer "
    "where perc_err > 1")


# Function for setting up the database connection
def retrieve_results(query):
    db = psycopg2.connect(database=Source_Name)
    cu = db.cursor()
    cu.execute(query)
    query_results = cu.fetchall()
    db.close()
    return query_results


# Function that displays the output
def display_results(answers):
    print (answers[0])
    for iter_val, q_answers in enumerate(answers[1]):
            print (
                "\t", iter_val+1, "->", q_answers[0],
                "\t - ", str(q_answers[1]), "views")


# Function that displays query 3 output
def display_q3_results(answers):
    print (answers[0])
    for q_answer in answers[1]:
        print ("\t", q_answer[0], "->", str(q_answer[1]) + "%")


# Retrieving the results and storing it in a list
query_1_answer = question_1, retrieve_results(query_1)
query_2_answer = question_2, retrieve_results(query_2)
query_3_answer = question_3, retrieve_results(query_3)

# Displaying the results
display_results(query_1_answer)
display_results(query_2_answer)
display_q3_results(query_3_answer)
