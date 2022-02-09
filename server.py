# Imports
# Importing Flask
from flask import Flask, render_template, redirect, url_for
# Setting up flask app - DO NOT TOUCH THIS LINE
app = Flask(__name__)
# App Name - Nhs Comp
# Begin!
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/admin/<id>')
def admin(id):
    if id == '1798':
        return 'status of app: '+app
    elif id == 'del':
        return 'https://postimg.cc/delete/jGyBDWSM/f1f475cc'
    else:
        return 'Access Denied'



# Run App - DO NOT TOUCH THIS LINE
if __name__ == '__main__':
    app.run(host='0.0.0.0')