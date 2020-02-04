import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='mz4358bh',
                             password='Compscispring2020',
                             db='mz4358bh_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
print("enter a name to search for: ")
user_input = input()

try:
    with connection.cursor() as cursor:
        # Select all Students
        sql = ("SELECT * from STUDENT where firstName = " + "'" + user_input + "'")

        # execute the SQL command
        cursor.execute(sql)

        # get the results
        for result in cursor:
            print(result)

        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes.
        # connection.commit()


finally:
    connection.close()