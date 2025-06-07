# Credit Card Fraud Detection System 


##  Credit Card Fraud Detection Using Machine Learning

This project presents a Flask-based web application designed to detect fraudulent credit card transactions using a machine learning model. With the increasing rate of online transactions, financial fraud has become a major concern. By leveraging supervised learning techniques, this project aims to provide a tool that can predict whether a transaction is likely to be fraudulent or not, based on various input features.

The backend of this application is powered by a pre-trained machine learning model (saved as `model.pkl`), which was trained on a dataset containing anonymized features of credit card transactions. The frontend is built using HTML and integrated with Flask to create a user-friendly interface, where users can input transaction data and receive immediate predictions.

This project is ideal for demonstrating the practical application of data science and machine learning in the domain of financial fraud prevention. It can be used for educational purposes, showcasing deployment of models, and understanding real-world use cases of ML in the banking and fintech sector.


###  About the Model:

The model used in this project was trained using scikit-learn. It uses anonymized transaction data that includes numerical features such as transaction amount, time, and engineered variables. The target variable is `isFraud`, indicating whether the transaction was legitimate (0) or fraudulent (1).


## 🛠 Installation and Setup Instructions

###  Prerequisites

Make sure you have the following installed:

* Python (3.7 or above)
* pip (Python package manager)
* Git (optional, for cloning)


  Step 1: Clone the Repository (ya ZIP extract karo)

```bash
git clone https://github.com/SumantraPrajapati/Credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

Agar ZIP file download ki hai:

* Extract karo
* Open the folder in terminal or command prompt


  Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it:

* **Windows:**

```bash
venv\Scripts\activate
```

* **Mac/Linux:**

```bash
source venv/bin/activate
```

###  Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

###  Step 4: Run the Flask App

```bash
python app.py
```

If `app.py` contains:

```python
app.run(debug=True)
```

You’ll see:

```
Running on http://127.0.0.1:5000/
```



###  Step 5: Open in Browser

Go to:

```
http://localhost:5000
```

Enter your transaction details, and see whether it predicts the transaction as **fraudulent** or **legitimate**.



###  Note

* Ensure `model.pkl` file is in the same folder as `app.py`
* If you face any `ModuleNotFoundError`, use `pip install` to fix it.


