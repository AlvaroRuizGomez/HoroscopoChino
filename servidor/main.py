from flask import Flask, render_template, request
app = Flask(__name__)


#rutas
@app.route('/', methods=['GET', 'POST'])
def home():
    # anyo = request.form['anyo']
    return render_template('index.html')


@app.route('/rata',methods=['GET', 'POST'])
def rata():
    # anyo = request.form['anyo']
    return render_template('rata.html')


if __name__ == "__main__":
    app.run('127.0.0.1', 5000, debug=True)