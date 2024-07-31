import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="guestbook",
        user="postgres",
        password="mysecretpassword"
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM entries;')
    entries = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', entries=entries)

@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO entries (title, content) VALUES (%s, %s)', (title, content))
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')

