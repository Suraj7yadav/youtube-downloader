from flask import Flask, render_template, url_for, request, redirect
from pytube import YouTube
import re

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/download',methods=['POST'])
def download():
    link = request.form['search'].strip()
    error=0
    try:
        yt = YouTube(link)
        vid = yt.streams.filter(progressive=True).first()
        vid.download()
    except:
        error=2
    if(not error):
        return render_template('index.html')
    else:
        return render_template('error.html')