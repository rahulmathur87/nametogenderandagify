from info import InfoBot
from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_endpoint = 'https://api.npoint.io/982b6858478d3009210b'
response = requests.get(blog_endpoint)
response.raise_for_status()
data = response.json()


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/guess/<name>")
def guess(name):
    info_bot = InfoBot(name)
    age = info_bot.get_age()
    gender = info_bot.get_gender()
    return render_template('guess.html', name=name, age=age, gender=gender)


@app.route("/blog/<num>")
def get_blog(num):
    return render_template('blog.html', data=data)


app.run(debug=True)
