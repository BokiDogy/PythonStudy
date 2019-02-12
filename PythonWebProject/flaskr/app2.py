from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/')
def index():
    username=request.args.get("username")
    return f'<p>Your username is {username}!<p>'

@app.route('/<name>')
def hello_world(name):
    return f'<h1>Hello {name}!<h1>'


if __name__ == '__main__':
    app.run(debug=True)
