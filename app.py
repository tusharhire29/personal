from flask import Flask, render_template, request
import os
import json

app = Flask(__name__)
app.secret_key = "PORTFOLIO WEBSITE"

#to blog 1
@app.route('/blog_single')
def blog_single() :
    file = 'comments.json'
    if os.path.exists(file) :
        with open(file, 'r') as r :
            comment_dict = json.load(r)
            comment_list = comment_dict['blog_single']
    else :
        comment_list = []

    return render_template('/blog_single', comment_list = comment_list)
    