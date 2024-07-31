from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection setup
def get_db_connection():
    conn = psycopg2.connect(
        host='db',  # The name of the service in your docker-compose file
        database='guestbook',
        user='postgres',
        password='yourpassword'
    )
    return conn

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO entries (name, message) VALUES (%s, %s)', (name, message))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT name, message FROM entries')
    entries = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', entries=entries)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

