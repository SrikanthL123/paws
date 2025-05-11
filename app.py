from flask import Flask, request, render_template
import pymysql

app = Flask(__name__)

# Connect to AWS RDS (edit values!)
db = pymysql.connect(
    host='db1.ci9ecqc4s3a2.us-east-1.rds.amazonaws.com',
    user='admin',
    password='Suhani4567',
    database='userdb'
)

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        feedback = request.form['feedback']

        cursor = db.cursor()
        sql = "INSERT INTO users (username, email, feedback) VALUES (%s, %s, %s)"
        cursor.execute(sql, (username, email, feedback))
        db.commit()

        return "Data saved successfully!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

