import random

from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

from happiness import calc_happiness
from recommendation import *

app = Flask(__name__, static_folder="./dist/static", template_folder="./dist")
CORS(app)

# デフォルト
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# '/rand'が叩かれた時、乱数を生成
@app.route('/rand')
def random_test():
    response = {
        'randomNum': random.random()
    }
    return jsonify(response)

@app.route('/get_recommend',methods=["POST"])
def get_recommend():
    data=request.get_json()
    # data形式は以下
    # {answer:["1","3","5","9",.....,"2"]}

    happiness = calc_happiness(data) # 地域-幸福度配列を返す
    recommendation = cal_recommendation(happiness) #幸福度が高い地域を降順に出力
    response = {}
    for i in range(len(recommendation)):
        response[i] = {
            "area": recommendation[i],
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
