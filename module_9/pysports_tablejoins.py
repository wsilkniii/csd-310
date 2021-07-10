
# William Silknitter
# July 1st, 2021
# Prof. Sampson
# PySports: Basic Table Joins

import mysql.connector
from mysql.connector import errorcode
from getch import pause_exit

config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    mycursor = db.cursor()

    sql = "SELECT player_id, first_name, last_name, team_name\
        FROM player \
        INNER JOIN team \
            ON player.team_id = team.team_id;"
    
    mycursor.execute(sql)

    myresults = mycursor.fetchall()

    print(" -- DISPLAYING PLAYER RECORDS == ")
    for result in myresults:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam ID: {}\n".format(result[0], result[1], result[2], result[3]))

    print("\n")
    pause_exit(0, "Press any key to continue...")



except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("     The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("     The specified database does not exist")
    
    else:
        print(err)

finally:
    db.close()
