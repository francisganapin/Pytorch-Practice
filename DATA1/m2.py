from flask import session,request,redirect,url_for,Flask

app = Flask(__name__)
app.secret_key = 'SAZXCK,ANEDKL1asdzxdf@'


# use this for username and password check if they are equal to those

VALID_USERNAME = 'admin'
VALID_PASSOWRD = 'password'

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return 'You are not logged in'

@app.route('/login',methods=['Get','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == VALID_USERNAME and password == VALID_PASSOWRD:
            session['username'] == username
            return redirect(url_for('index'))
        else:
            return "Invalid username or password. <a href='/login'>Try again</a>"
    
    return '''
    <form method='post'>
        <p><input type=text name=username>
        <p><input type=password name=password>
        <p><input type=submit value=Login>
    </form>
'''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)