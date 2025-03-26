import json

from flask import Flask

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
            "age":10
        },
        {
            "no":"C002",
            "name":"Michelin",
            "age":8
        }
    ]

    customers_json = json.dumps(customers)
    return customers_json

@app.route('/api/customerledgerentry')
def customerledgerentry():
    return "customerledgerentry"

if __name__ == '__main__':
    app.run()