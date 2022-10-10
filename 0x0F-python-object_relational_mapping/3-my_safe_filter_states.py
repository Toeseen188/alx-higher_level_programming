#!/usr/bin/python3
""" a script that lists all states from the database hbtn_0e_0_usa
# search for state provided as argument
# save from sql injection
# Usage: ./3my_safe_filter_states.py root root hbtn_0e_0_usa 'states'
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    search = sys.argv[4]
    q = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(q)
    states = cursor.fetchall()
    for state in states:
        if state[1] == search:
            print(state)
    cursor.close()
    conn.close()
