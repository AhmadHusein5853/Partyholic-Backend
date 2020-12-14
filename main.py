
# import re # delete it if you don't need it later , maybe you need it in other class
# from nltk.tokenize import TweetTokenizer
from flask import Flask, request, jsonify

app = Flask(__name__)

def get_image(request):
    data=request.get_data()
    name_of_photo=request.remote_addr
    with open(str(name_of_photo)+".jpg","wb") as f:
        f.write(data)
    return str(name_of_photo)+".jpg"

@app.route('/', methods=['POST'])
def post():
    result_dict = {}

    result_dict.update({"We get":get_image(request)})

    #result_dict= str(result_dict)    just to make it recived in one line
    return jsonify(result_dict)


@app.route('/', methods=['GET'])
def index():
    return "<h1>No POST request found !!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=8080)