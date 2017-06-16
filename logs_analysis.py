#! /usr/bin/env python3
import psycopg2
#  Variable to store db name
Source_Name = "news"
#  Question1 & it's answer
question_1 = ("What are the three most popular articles of all time")
query_1 = ("select title,visit_count from info_view limit 3 ")


#  Function for setting up the database connection
def retrieve_results(query):
    db = psycopg2.connect(database=Source_Name)
    cu = db.cursor()
    cu.execute(query)
    query_results = cu.fetchall()
    db.close()
    return query_results


#  Function that displays the output
def display_results(answers):
    print (answers[0])
    for iter_val, q_answers in enumerate(answers[1]):
            print (
                "\t", iter_val+1, "->", q_answers[0],
                "\t - ", str(q_answers[1]), "views")


#  Retrieving the results and storing it in a list
query_1_answer = question_1, retrieve_results(query_1)
#  Displaying the results
display_results(query_1_answer)
