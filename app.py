from flask import Flask, request, render_template, redirect, url_for
import polars as pl
from src.create_csv_bytes_object_from_dataframe \
    import create_csv_bytes_object_from_dataframe

app = Flask(__name__)


# For testing Postman connectivity, only
# @app.route('/')
# def home():
#     return "Postman check successful"
@app.route('/')
def home():
    return "Main page"

@app.route('/upload', methods = ['GET','POST'])
def upload_table():

    if request.method == 'POST':
        return redirect(url_for('download'))

        # data = request.get_json()
        # df = pl.DataFrame(data)
        # csv_bytes = create_csv_bytes_object_from_dataframe(df)
        # return send_file(
        #     csv_bytes,
        #     mimetype='text/csv',
        #     as_attachment=True,
        #     attachment_filename=f'{table_id}.csv'
        # )
    return render_template('upload_csv.html')
        


if __name__ == '__main__':
    app.run(debug = True)