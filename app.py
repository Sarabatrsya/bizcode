import pandas as pd
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/MOF')
def get_data():
    # Load data from the Excel file
    #http://localhost:5000/MOF
    excel_file = 'Excel/mof.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/CIDB')
def get_data2():
    # Load data from the Excel file
    #http://localhost:5000/CIDB
    excel_file = 'Excel/CIDB.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

@app.route('/NEWTERM')
def get_data3():
    # Load data from the Excel file
    #http://localhost:5000/NEWTERM
    excel_file = 'Excel/KAMUS MSIC.xlsx'  # Replace with your file name
    df = pd.read_excel(excel_file)

    # Convert data to a list of dictionaries
    data = df.to_dict(orient='records')

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
