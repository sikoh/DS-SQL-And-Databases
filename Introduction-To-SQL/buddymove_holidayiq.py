import sqlite3
import pandas as pd

buddy_df = pd.read_csv('Introduction-To-SQL/buddymove_holidayiq.csv')
buddy_df = buddy_df.rename(columns = {"User Id": "User_id"})

conn = sqlite3.connect("Introduction-To-SQL/buddymove_holidayiq.sqlite3")
curs = conn.cursor()

buddymove = buddy_df.to_sql("buddymove", con=conn, if_exists="replace")

query_all = "SELECT COUNT(*) FROM buddymove"
query_count = "SELECT COUNT(User_id) FROM buddymove WHERE Nature >= 100 AND Shopping >= 100"

def execute_query(some_query):
    curs.execute(some_query)
    result = curs.fetchall()
    return result[0][0]

print(execute_query(query_all))
print(execute_query(query_count))