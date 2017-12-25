import os
import json

from flask import Flask
from flask import request

from sklearn.datasets import load_iris
from sklearn import tree

app = Flask(__name__)


def trainML():
    print("Training Started!")
    iris = load_iris()
    # print(iris.data[60])
    # print(iris.target[60])
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(iris.data, iris.target)
    print("Training Completed!")
    return clf


clf = trainML()


@app.route('/webhook', methods=['POST'])
def webhook():
    body = request.get_json()
    print("body: ", body)

    data = body['result']['parameters']
    print("data: ", data)

    sLength = data['sLength']
    sWidth = data['sWidth']
    pLength = data['pLength']
    pWidth = data['pWidth']

    result = clf.predict([[sLength, sWidth, pLength, pWidth]])

    print("result: ", result)
    head = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

    return json.dumps({
        "speech": "<speak> " +
                  "<s> Ok you said </s> " +
                  "<s> sepal length is  " + sLength + "cm </s>" +
                  "<s> sepal width is  " + sWidth + "cm </s>" +
                  "<s> petal length is  " + pLength + "cm </s>" +
                  "<s> and </s>" +
                  "<s> petal width is  " + pWidth + "cm. </s>" +
                  "<s> it looks like this flower belongs from " + head[result[0]] + " </s>" +
                  "</speak>"
    })


if __name__ == '__main__':
    app.run(port=4000)
