from flask import Flask,request,flash,redirect,url_for,render_template

app = Flask(__name__)
app.secret_key = 'loki'

@app.route('/login', methods=['GET','POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
                request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again !'
        else:
            flash('you were sucesffuly logged in')
            return redirect(url_for('index'))
    return render_template('login.html',error=error)

@app.route('/index')
def index():
    return 'Welcome to the index Page'

if __name__ == '__main__':
    app.run(debug=True)