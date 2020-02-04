from flask import Flask, render_template
import pymysql
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='mz4358bh',
                             password='Compscispring2020',
                             db='mz4358bh_University',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Select from Students Table the name set as input
        sql = ("SELECT * from STUDENT")

        # execute the SQL command
        cursor.execute(sql)
        output = cursor.fetchall()

finally: connection.close()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'


@app.route('/dbconnect')
def dbconnect():
    return render_template('dbconnect.html', output=output)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4358)