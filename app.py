"""
Allows user to select local JSON file for upload, which is then converted to
a DataFrame, before being converted to a CSV file and uploaded to
the uploaded_files folder
"""

import os
import datetime as dt
import polars as pl
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename

app = Flask(__name__)


ALLOWED_EXTENSIONS = "json"

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    return "Main page"


@app.route("/upload", methods=["GET", "POST"])
def upload_table():

    if request.method == "POST":

        file = request.files["file"]
        if file and allowed_file(file.filename):
            
            transition_df = pl.read_json(file)

            filename = secure_filename(file.filename)
            new_filename = f"{
                filename.split(".")[0]}_{
                str(
                    dt.datetime.now().isoformat(
                        timespec = "hours"))}.csv"
            save_location = os.path.join("uploaded_files", new_filename)

            transition_df.write_csv(save_location)

    return render_template("upload_csv.html")


if __name__ == '__main__':
    app.run()
