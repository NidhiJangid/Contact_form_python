from flask import Flask, request, render_template,jsonify, make_response,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'coding thunder'
mysql = MySQL(app)


@app.route("/", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        userDetails = request.form
        sno = userDetails['sno']
        name = userDetails['name']
        msg = userDetails['msg']
        date = userDetails['date']
        cur = mysql.connection.cursor()
        cur.execute('INSERT into contactw(sno,name,msg,date)VALUES(%d,%s,%s,%d)', (sno, name, msg, date))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


@app.route('/users',methods=['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    resultvalue = cur.execute("SELECT * FROM contactw")
    if resultvalue > 0:
        userDetails = cur.fetchall()
        # return render_template('index.html', userDetails=userDetails)
        response = make_response(
            jsonify({"data": userDetails}), 200)
        response.headers["Content-Type"] = "application/json"
    return response


if __name__ == '__main__':
    app.run(debug=True, port=9090)
