from flask import Flask, request, jsonify

app = Flask(__name__)
expenses = []

@app.route('/expenses', methods=['GET'])
def get_expenses():
    return jsonify(expenses)

@app.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    expenses.append(data)
    return jsonify({'message': 'Expense added'}), 201

@app.route('/expenses', methods=['DELETE'])
def delete_expenses(index):
    if index < len(expenses):
        expenses.pop(index)
        return jsonify({'message': 'Deleted'}), 200
    return jsonify({'error': 'Not found'}), 404

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')

