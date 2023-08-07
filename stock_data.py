import os
import pandas as pd
from flask import Flask, jsonify
import json
import numpy as np
import yfinance as yf

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

@app.route('/historicaldata/stock/<string:ticker>', methods=['GET'])
def get_historical_data(ticker):
    print(ticker)
    try:
        # Faz o download dos dados históricos da ação usando o yfinance
        df = yf.download(ticker, start='2015-01-01')
        # Transforma o DataFrame em um dicionário
        historical_data = df.to_dict(orient='records')
        # Retorna a resposta JSON diretamente usando a função jsonify do Flask
        return jsonify(historical_data)

    except Exception as e:
        # Em caso de erro, retorna uma resposta de erro
        error_response = {
            'error': str(e)
        }
        return jsonify(error_response), 500

if __name__ == '__main__':
    app.run(debug=True)
