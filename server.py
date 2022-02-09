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
@app.route('/about')
def about_surgeon():
    return render_template('about.html')

# Admin Controls
@app.route('/admin/git')
def git():
    return redirect('https://github.com/v-mod/nhs-comp.git')

@app.route('/admin/code')
def code():
    return redirect('https://vscode.dev/github/v-mod/nhs-comp')
@app.route('/admin/app/<id>')
def admin(id):
    if id == '1798':
        return "(host='0.0.0.0', port='443', debug=True, ssl_context=('certificate.crt','private.key')"
    elif id == 'del':
        return 'https://postimg.cc/delete/jGyBDWSM/f1f475cc'
    else:
        return 'Access Denied'


# Run App - DO NOT TOUCH THIS LINE
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='443', debug=True, ssl_context=('certificate.crt','private.key'))
