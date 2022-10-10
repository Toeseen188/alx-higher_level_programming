#!/usr/bin/python3
# a script that lists all cities from the database hbtn_0e_4_usa
# Usage: ./4-cities_by_state.py root root hbtn_0e_4_usa
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    INNER JOIN states ON cities.state_id = states.id\
                    ORDER BY cities.id")
    for cities in cursor.fetchall():
        print(cities)
    cursor.close()
    conn.close()
