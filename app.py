import sqlite3
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcdefghij'

def get_db_connection():
    conn = sqlite3.connect('filmflix.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_film(filmID):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM tblFilms WHERE filmID = ?',
                        (filmID,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Get the selected sorting criteria from the request
    sort_by = request.form.get('sort_by', 'title')
    print(f'Sort By: {sort_by}')
    # Define a dictionary to map the sorting criteria to column names
    sort_columns = {
        'title': 'title',
        'yearReleased': 'yearReleased',
        'rating': 'rating',
        'duration': 'duration'
    }
    # Check if the selected sorting criteria is valid
    if sort_by in sort_columns:
        sort_column = sort_columns[sort_by]
        sql_query = f'SELECT filmID, title, yearReleased, rating, duration, genre FROM tblFilms ORDER BY {sort_column} ASC'
        print(f'SQL Query: {sql_query}')
        cursor.execute(sql_query)
    else:
        # Handle the case when the sorting criteria is invalid
        cursor.execute('SELECT filmID, title, yearReleased, rating, duration, genre FROM tblFilms')
    posts = cursor.fetchall()
    conn.close()
    return render_template('index.html', posts=posts)


@app.route('/create.html', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        yearReleased = request.form['yearReleased']
        duration = request.form['duration']
        rating = request.form['rating']
        genre = request.form['genre']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO tblFilms (title, yearReleased, duration, rating, genre) VALUES (?, ?, ?, ?, ?)',
                         (title, yearReleased, duration, rating, genre))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:filmID>/edit', methods=('GET', 'POST'))
def edit(filmID):
    post = get_film(filmID)
    if request.method == 'POST':
        title = request.form['title']
        yearReleased = request.form['yearReleased']
        duration = request.form['duration']
        rating = request.form['rating']
        genre = request.form['genre']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE tblFilms SET title = ?, yearReleased = ?, duration = ?, rating = ?, genre = ?'
                         ' WHERE filmID = ?',
                         (title, yearReleased, duration, rating, genre, filmID))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
    return render_template('edit.html', post=post)

@app.route('/<int:filmID>/delete', methods=('POST',))
def delete(filmID):
    post = get_film(filmID)
    conn = get_db_connection()
    conn.execute('DELETE FROM tblFilms WHERE filmID = ?', (filmID,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run()
