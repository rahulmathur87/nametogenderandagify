from info import InfoBot
from flask import Flask, render_template

# name = input("Input name : ")

#
# print(f"Hey {name}\n"
#       f"I think you are {info_bot.get_gender()}\n"
#       f"And maybe {info_bot.get_age()} years old.")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/guess/<name>")
def guess(name):
    info_bot = InfoBot(name)
    age = info_bot.get_age()
    gender = info_bot.get_gender()
    return render_template('guess.html', name=name, age=age, gender=gender)


app.run(debug=True)
