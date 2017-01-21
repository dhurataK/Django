import random

from old_mysqlconnection import MySQLConnector

mysql = MySQLConnector("friends")

first_names = ["Noah", "Liam", "Mason", "Jacob", "William", "Ethan", "Michael", "Alexander", "James", "Daniel", "Emma", "Olivia", "Sophia", "Isabella", "Ava", "Mia", "Emily", "Abigail", "Madison", "Charlotte"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson", "Martinez", "Anderson", "Taylor", "Thomas", "Hernandez", "Moore", "Martin", "Jackson", "Thompson", "Lopez", "Lee", "Gonzalez", "Harris"]

names = [(first, last) for first in first_names for last in last_names]

relationships = {(i,j) for i in range(1,16) for j in range(1,16) if i != j}

"""
# Insert names
for first_name, last_name in random.sample(names, 15):
	query = "INSERT INTO users (first_name, last_name, created_at, updated_at) VALUES ('{}', '{}', NOW(), NOW())".format(first_name, last_name)
	mysql.run_mysql_query(query)
"""

# Make symmetrical friendships
for count in range(15):
	user, friend = relationships.pop()
	mysql.run_mysql_query("INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES ({}, {}, NOW(), NOW())".format(user, friend))
	mysql.run_mysql_query("INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES ({}, {}, NOW(), NOW())".format(friend, user))
	relationships.discard((friend, user))

# Make asymmetric friendships
for user, friend in random.sample(relationships, 20):
	mysql.run_mysql_query("INSERT INTO friendships (user_id, friend_id, created_at, updated_at) VALUES ({}, {}, NOW(), NOW())".format(user, friend))