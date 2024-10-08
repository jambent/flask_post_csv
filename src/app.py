from flask import Flask, request
from create_csv_bytes_object_from_dataframe \
    import create_csv_bytes_object_from_dataframe

app = Flask(__name__)


# For testing Postman connectivity, only
# @app.route('/')
# def home():
#     return "Postman check successful"


@app.route('/tables/<table_id>', methods = ['GET', 'POST'])
def table(table_id):
    if request.method == 'GET':

    if request.method == 'POST':
        


if __name__ == '__main__':
    app.run()