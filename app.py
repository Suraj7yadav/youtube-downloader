from flask import Flask, render_template, url_for, request, redirect, flash
from pytube import YouTube
import re,os

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
        fold = os.path.join(os.getenv('USERPROFILE'), 'Downloads')
        vid.download(fold)
        flash("Downloaded successfully")
    except:
        error=2
    if(not error):
        return render_template('index.html')
    else:
        return render_template('error.html')
