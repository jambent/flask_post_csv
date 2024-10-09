"""
Allows user to POST data to /upload endpoint, the data being
echoed back as a JSON object
"""

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/upload", methods=["GET", "POST"])
def upload_table():

    if request.method == "POST":

        input_data = request.data
        input_data_str = input_data.decode('utf-8')

    return jsonify({'post_body': input_data_str})


if __name__ == '__main__':
    app.run()
