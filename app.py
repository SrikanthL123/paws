from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Connect to AWS RDS (edit values!)
db = pymysql.connect(
    host='YOUR-RDS-ENDPOINT',
    user='admin',
    password='yourpassword',
    database='userdb'
)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']

        cursor = db.cursor()
        sql = "INSERT INTO users (username, email) VALUES (%s, %s)"
        cursor.execute(sql, (username, email))
        db.commit()

        return "Data saved successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

