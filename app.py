from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

API_URL = 'https://api.premiumy.net/v1.0'
API_KEY = 'Wdv1qTghQJ2sKzp5Q_4Tcg'

@app.route('/live_calls', methods=['GET'])
def get_live_calls():
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': API_KEY
    }
    payload = {
        "id": None,
        "jsonrpc": "2.0",
        "method": "live_call:get_list_by_account_user",
        "params": {}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    return jsonify(data['result']['live_call_list'])

@app.route('/cdr_cost', methods=['POST'])
def get_cdr_cost():
    headers = {
        'Content-Type': 'application/json',
        'Api-Key': API_KEY
    }
    filter_data = request.json
    payload = {
        "id": None,
        "jsonrpc": "2.0",
        "method": "cdr_full:group_get_list",
        "params": {
            "filter": filter_data,
            "group": "range/a_number/b_number",
            "page": 1,
            "per_page": 15
        }
    }
    response = requests.post(f"{API_URL}/csv", headers=headers, json=payload)
    data = response.json()
    cost = data['result']['group_summaries']['cost']
    return jsonify({'cost': cost})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
