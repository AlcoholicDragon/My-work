import mysql.connector as msc
connection = msc.connect(user="root",
                         password="DragonKing29",
                         host= '127.0.0.1',
                         database='fairytail')
def col():
    if (connection.is_connected()):
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM members;")
        record = cursor.fetchall()
        for i in record:
            print(i)
        cursor.close()
        connection.close()
        return
col()
