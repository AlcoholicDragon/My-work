import mysql.connector as msc

connection_config_dict = {
    'user': 'root',
    'password': 'DragonKing29',
    'host': '127.0.0.1',
    'database': 'fairytail',
    'raise_on_warnings': True,
    'autocommit': True,
    'pool_size': 5
}
connection = msc.connect(**connection_config_dict)
if (connection.is_connected()):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM members;")
    record = cursor.fetchall()
    for i in record:
        print(i)
    cursor.close()
    connection.close()
