from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from keras.models import load_model

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('pages/dashboard.html')

@app.route('/home', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        df = pd.read_csv(request.files.get('file'))
        data_table = df.to_html()
        return render_template('home.html', table=data_table)
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
