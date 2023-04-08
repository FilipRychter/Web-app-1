from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)



@app.route('/')
def hello_world():
    return render_template('home.html')
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/sign-up')
def sign_up():
    return render_template('sign-up.html')

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
