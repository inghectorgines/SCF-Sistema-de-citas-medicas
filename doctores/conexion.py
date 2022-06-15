import mysql.connector

def conect():
    database = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "scf_script",
    )
    cursor = database.cursor(buffered = True)
    return [database, cursor]
