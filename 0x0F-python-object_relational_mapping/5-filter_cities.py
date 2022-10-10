#!/usr/bin/python3
""" a script that lists all cities of a searched states
# from the database hbtn_0e_4_usa
# Usage: ./5-filter_cities.py root root hbtn_0e_4_usa states
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    search = sys.argv[4]
    ans = []
    conn = MySQLdb.connect(host="localhost", port=3306,  user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cursor = conn.cursor()
    cursor.execute("""SELECT cities.name FROM cities
                    INNER JOIN states ON cities.state_id = states.id
                    WHERE states.name =%s ORDER BY cities.id""", (search, ))
    for cities in cursor.fetchall():
        ans.append(cities[0])
    print(", ".join(ans))
    cursor.close()
    conn.close()
