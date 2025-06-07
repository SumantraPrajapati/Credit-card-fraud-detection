from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)   # ✅ Yeh line sabse zaroori hai

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # 1. Get input values from form
    amount = float(request.form['amount'])
    oldbalanceOrg = float(request.form['oldbalanceOrg'])
    oldbalanceDest = float(request.form['oldbalanceDest'])
    transaction_type = request.form['type']

    # 2. Derived features
    org_balance_diff = oldbalanceOrg - amount
    dest_balance_diff = 0  # Not input from form
    isReceiverBalanceSame = 1  # Assume yes

    # 3. One-hot encoding of transaction type
    type_CASH_OUT = 1 if transaction_type == 'CASH_OUT' else 0
    type_DEBIT = 1 if transaction_type == 'DEBIT' else 0
    type_PAYMENT = 1 if transaction_type == 'PAYMENT' else 0
    type_TRANSFER = 1 if transaction_type == 'TRANSFER' else 0

    # 4. Prepare input
    final_input = np.array([[amount, oldbalanceOrg, oldbalanceDest,
                             org_balance_diff, dest_balance_diff, isReceiverBalanceSame,
                             type_CASH_OUT, type_DEBIT, type_PAYMENT, type_TRANSFER]])

    prediction = model.predict(final_input)
    result = "🚨 Fraud Transaction Detected!" if prediction[0] == 1 else "✅ Valid Transaction"

    return render_template('index.html', prediction_text=result)

if __name__ == '__main__':
    app.run(debug=True)
