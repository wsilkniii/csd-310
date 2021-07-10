
# William Silknitter
# July 1st, 2021
# Prof. Sampson
# PySports: Updates and Deletes

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

    insert = "INSERT INTO player (first_name, last_name, team_id) \
            VALUES('Luffy','Monkey', 2);"
    
    mycursor.execute(insert)

    verification = "SELECT player_id, first_name, last_name, team_name\
        FROM player \
        INNER JOIN team \
            ON player.team_id = team.team_id;"

    mycursor.execute(verification)

    myresults = mycursor.fetchall()

    print("\n")
    print(" -- DISPLAYING PLAYERS AFTER INSERT -- ")
    print("\n")
    for result in myresults:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(result[0], result[1], result[2], result[3]))

    update = "UPDATE player \
        SET team_id = 1, \
            first_name = 'Luffy', \
            last_name = 'Monkey' \
        WHERE first_name = 'Luffy';"

    mycursor.execute(update)

    verification = "SELECT player_id, first_name, last_name, team_name\
        FROM player \
        INNER JOIN team \
            ON player.team_id = team.team_id;"

    mycursor.execute(verification)
    
    myresults = mycursor.fetchall()

    print("\n")
    print(" -- DISPLAYING PLAYERS AFTER UPDATE -- ")
    print("\n")
    for result in myresults:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(result[0], result[1], result[2], result[3]))


    delete = "DELETE FROM player \
        WHERE first_name = 'Luffy';"

    mycursor.execute(delete)
    
    verification = "SELECT player_id, first_name, last_name, team_name\
        FROM player \
        INNER JOIN team \
            ON player.team_id = team.team_id;"

    mycursor.execute(verification)

    myresults = mycursor.fetchall()

    print("\n")
    print(" -- DISPLAYING PLAYERS AFTER DELETE -- ")
    print("\n")
    for result in myresults:
        print("Player ID: {}\nFirst Name: {}\nLast Name: {}\nTeam Name: {}\n".format(result[0], result[1], result[2], result[3]))

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
