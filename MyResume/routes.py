from flask import render_template
from MyResume import app

@app.route('/homepage')
@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
