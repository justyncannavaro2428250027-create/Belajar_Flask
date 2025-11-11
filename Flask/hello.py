# import flash module
from turtle import title
from flask import Flask, render_template
# create an instance of the Flask class
app = Flask(__name__, template_folder='views')
# define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# define a route for the about page
@app.route('/about')
def about():
    title = "About Page"
    return render_template('about.html', title = title)

@app.route('/contact')
def contact():
    title = "Contact Page"
    return render_template('contact.html', title = title)

@app.route('/pendaftaran')
def pmb():
    title = "Pendaftaran Mahasiswa Baru"
    return render_template('pmb.html', title = title)
# run the application
if __name__ == '__main__':
    app.run(debug=True)