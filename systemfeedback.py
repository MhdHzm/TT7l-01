from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Database setup
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS Feedback (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, message TEXT)')
        conn.execute('CREATE TABLE IF NOT EXISTS Support (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, issue TEXT)')
    print("Tables created successfully")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Feedback (name, email, message) VALUES (?, ?, ?)", (name, email, message))
            conn.commit()
            flash('Thank you for your feedback!')
        
        return redirect(url_for('feedback'))
    
    return render_template('feedback.html')

@app.route('/support', methods=['GET', 'POST'])
def support():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        issue = request.form['issue']
        
        with sqlite3.connect('database.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO Support (name, email, issue) VALUES (?, ?, ?)", (name, email, issue))
            conn.commit()
            flash('Your support request has been received. We will contact you soon.')
        
        return redirect(url_for('support'))
    
    return render_template('support.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
