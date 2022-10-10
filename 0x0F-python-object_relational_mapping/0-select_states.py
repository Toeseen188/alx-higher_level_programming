#!/usr//bin/python3
# a script that lists all states from the database hbtn_0e_0_usa
# Usage: ./0-select_states.py root root hbtn_0e_0_usa
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    conn.close()
