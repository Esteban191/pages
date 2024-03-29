
from flask import Flask, render_template

app = Flask(__name__, static_folder='templates', static_url_path='/templates')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


