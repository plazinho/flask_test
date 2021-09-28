from flask import Flask, render_template

from api.musicmatcher import rec_music
from static.texts import HEADER

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'Привет', 200
    # return render_template('index.html', header=HEADER), 200


@app.route('/result', methods=['GET'])
def music_match():
    result = rec_music()
    return result, 200
    # return render_template('index.html', header=HEADER), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
