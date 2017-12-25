import os

from flask import Flask
from flask import request

from sklearn.datasets import load_iris
from sklearn import tree

import json
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():

    body = request.get_json()
    print("body: ", body)

    data = body['result']['parameters']
    print("data: ", data)

    sLength = data['sLength']
    pLength = data['pLength']
    sWidth = data['sWidth']
    pWidth = data['pWidth']

    result = guessFlower(sLength, pLength, sWidth, pWidth)


    head = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

    return json.dumps({
        "speech": "this is " + head[result[0]]
    })



def trainML():
    iris = load_iris()
    print(iris.data[60])
    print(iris.target[60])

    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)
    print("Training Done!")
    return clf


clf = trainML()


def guessFlower(sLength, pLength, sWidth, pWidth):
    return clf.predict([[sLength, pLength, sWidth, pWidth]])


if __name__ == '__main__':
    app.run(port=4000)
