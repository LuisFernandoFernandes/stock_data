import os
import pandas as pd
from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/tickers', methods=['GET'])
def get_tickers():
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data', 'tickers.csv')
    df = pd.read_csv(csv_file_path, encoding='utf-8')
    tickers = df.to_dict(orient='records')

    # Converter para JSON com codificação correta (utf-8)
    json_data = json.dumps(tickers, ensure_ascii=False).encode('utf-8')
    response = app.response_class(
        response=json_data,
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run(debug=True)
