from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return(render_template('home.html'))


@app.route('/bagging/')
def bagging():
    return(render_template('bagging.html'))


@app.route('/measuring/')
def measuring():
    return(render_template('measuring.html'))


@app.route('/threshing/')
def threshing():
    return(render_template('threshing.html'))


@app.route('/seasons/')
def seasons():
    return(render_template('seasons.html'))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
