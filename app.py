import json
from datetime import datetime

from flask import Flask

from demo_basic import formatdatetime

app = Flask(__name__)

@app.route('/api/home')
def home():
    return "欢迎光临"

@app.route('/api/customers')
def customer():
    customers=[
        {
            "no":"C001",
            "name":"Porsche",
            "age":10,
            "createdt":formatdatetime(datetime.now())
        },
        {
            "no":"C002",
            "name":"Michelin",
            "age":8,
            "createdt":formatdatetime(datetime.now())
        }
    ]

    customers_json = json.dumps(customers)
    return customers_json

@app.route('/api/customerledgerentry')
def customerledgerentry():
    return "customerledgerentry"

if __name__ == '__main__':
    app.run()