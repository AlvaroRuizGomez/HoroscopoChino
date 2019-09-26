from flask import Flask, render_template
app = Flask(__name__)


#rutas
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/rata')
def rata():
    return render_template('rata.html')


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)