# import flash module
import email
from turtle import title
from urllib import request
from flask import Flask, render_template
from flask import request
import os
import time

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        #Proses data form di sini
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']

        #Tampilan pada terminal
        print(f"Nama: {nama}, Email: {email}, Pesan: {pesan}")
        
    title = "Contact Page"
    return render_template('contact.html', title = title)

@app.route('/pendaftaran', methods = ['GET', 'POST'])
def pmb():
    if request.method == 'POST':
        #ambil data dari form pendaftaran
        nama = request.form['nama']
        email = request.form['email']
        tempat_lahir = request.form['tempatLahir']
        tanggal_lahir = request.form['tanggalLahir']
        asal_sma = request.form['asalSekolah']
        foto = request.files['foto']

        #upload foto ke folder 'uploads'
        foto.save(f'static/uploads/{foto.filename}')

        #Tampilkan pada terminal
        print(f'Nama: {nama}, Email: {email}, Tempat Lahir: {tempat_lahir}, Tanggal Lahir: {tanggal_lahir}, Asal SMA : {asal_sma}, Foto: {foto.filename}')
    title = "Pendaftaran Mahasiswa Baru"
    return render_template('pmb.html', title = title)
# run the application
if __name__ == '__main__':
    app.run(debug=True)