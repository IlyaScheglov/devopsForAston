from flask import Flask, request, jsonify
import psycopg2
import os

app = Flask(__name__)

# Подключение к базе данных
DATABASE_URL = os.getenv("DATABASE_URL", "dbname=BANK_DB user=BANK_DB password=BANK_DB")
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

@app.route('/accounts', methods=['GET'])
def get_accounts():
    cur.execute("SELECT * FROM accounts")
    accounts = cur.fetchall()
    return jsonify(accounts)

@app.route('/accounts', methods=['POST'])
def create_account():
    data = request.json
    cur.execute("INSERT INTO accounts (client_name, balance) VALUES (%s, %s) RETURNING id",
                (data['client_name'], data['balance']))
    account_id = cur.fetchone()[0]
    conn.commit()
    return jsonify({"id": account_id}), 201

@app.route('/accounts/<int:id>', methods=['DELETE'])
def delete_account(id):
    cur.execute("DELETE FROM accounts WHERE id = %s", (id,))
    conn.commit()
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
