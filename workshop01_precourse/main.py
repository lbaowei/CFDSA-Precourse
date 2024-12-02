import random
from flask import Flask, render_template

text_to_display_arr = ["Logic will get you from A to B. Imagination will take you everywhere.",
    "There are 10 kinds of people. Those who understand binary and those who don't.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies and the other is to make it so complicated that there are no obvious deficiencies.",
    "It's not that I'm so smart, it's just that I stay with problems longer.",
    "It is pitch dark. You are likely to be eaten by a grue."]

app = Flask(__name__)

@app.route('/')
def home():
    chosen_header = random.choice(text_to_display_arr)
    return render_template('index.html', header=chosen_header)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)