from flask import session,request,redirect,url_for,Flask

app = Flask(__name__)
app.secret_key = 'asdasqwexzz1@'

@app.route('/')
def index():
    if 'username' in session:
        return f"Logged in as {session['username']}"
    return 'You are not logged in'

@app.route('/login',methods=['Get','POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))

    return '''
    <form method='post'>
        <p><input type=text name=username>
        <p><input type=submit value=Login>
    </form>
    '''

@app.route('/logout')
def logout():
    session.pop('username',None)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
