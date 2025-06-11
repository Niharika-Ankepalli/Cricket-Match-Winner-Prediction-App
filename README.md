# 🏏 Cricket Match Outcome and Runs Prediction using Machine Learning & Neural Networks

This project aims to predict the **total runs scored in the first innings** of a cricket match and the **winning team**, using **Machine Learning (ML)** and **Neural Networks (NN)**. The goal is to support analysis and decision-making for cricket enthusiasts, analysts, and fantasy league players.

---

## 📌 Objectives

- Predict the **first innings total runs** using regression models.
- Predict the **match winner** using classification models.
- Build a user-friendly **Streamlit app** for interactive predictions.
- Train models on **real match data** with accurate results.
- Deploy the app online using **Streamlit Cloud**.

---

## 📂 Project Structure

cricket-prediction/
├── app.py # Main Streamlit app
├── run_predictor.py # Backend logic for model inference
├── dataset.csv # Cleaned match dataset
├── model.pkl # Trained model for runs prediction
├── neural_model.h5 # Trained neural network model for winner prediction
├── requirements.txt # List of required Python libraries
├── README.md # Project description file
├── utils/ # Supporting functions or preprocessing
└── .gitignore # Files excluded from GitHub

yaml
Copy
Edit

---

## 🧠 Problem Statement

Cricket is influenced by many variables: team composition, ground type, toss decision, and performance during the match. Manually predicting match outcomes is challenging. This project uses data-driven modeling to forecast:

1. The **expected number of runs** in the first innings.
2. The **likely winner** based on match conditions.

---

## 🧪 Models Used

### 1. First Innings Runs Prediction (Regression)
- **Features**: Batting team, bowling team, venue, overs, wickets
- **Models**:
  - Linear Regression
  - XGBoost Regressor
- **Evaluation**: R² Score, Mean Squared Error

### 2. Match Winner Prediction (Classification)
- **Features**: Toss winner, venue, innings total, team info
- **Models**:
  - Logistic Regression
  - XGBoost Classifier
  - Neural Network (Keras + TensorFlow)
- **Evaluation**: Accuracy Score, Confusion Matrix, Classification Report

---

## 📊 Dataset Information

- The dataset contains past match records with cleaned and encoded features.
- Sample columns:
  - `batting_team`, `bowling_team`, `venue`, `overs`, `wickets`, `total_runs`, `winner`, `toss_winner`, etc.
- Personal or confidential data is excluded.
- Data is preprocessed using one-hot encoding, label encoding, and normalization.

---

## 💻 How to Run the Project

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/cricket-prediction.git
cd cricket-prediction
2. (Optional) Create a Virtual Environment
bash
Copy
Edit
python -m venv env
source env/bin/activate        # On Windows: env\Scripts\activate
3. Install Required Libraries
bash
Copy
Edit
pip install -r requirements.txt
4. Launch the App
bash
Copy
Edit
streamlit run app.py
🧾 Sample Input (via Web App)
Batting team: India

Bowling team: Australia

Venue: Mumbai

Overs: 12.3

Wickets fallen: 3

Toss winner: India

First innings total: 180

🎯 Sample Output
Predicted Runs (1st Innings): 178

Predicted Match Winner: India

⚙️ Tools & Libraries
Library/Tool	Purpose
Pandas, NumPy	Data handling and manipulation
Matplotlib, Seaborn	Visualizations
scikit-learn	ML models and evaluation
XGBoost	Boosting model for regression/classification
TensorFlow, Keras	Deep learning & neural networks
Streamlit	Web app framework

🌐 Deployment (Streamlit Cloud)
To deploy your app online:
Push your code to a public GitHub repository.

Go to: https://streamlit.io/cloud

Click on “Deploy an app”

Connect your GitHub and select the repo.

Set the main file path as: app.py

Click Deploy.

✅ You will get a public link to share your app.

🚫 Notes on Privacy and GitHub
.env, passwords, or secret keys are excluded using .gitignore

The uploaded dataset is a sample and cleaned version — not real confidential data.

Large files (>100MB) are not pushed to GitHub.

📃 License
This project is licensed under the MIT License, which allows open usage with attribution.

yaml
Copy
Edit

---

This version is:

✅ Detailed  
✅ Professional  
✅ Privacy-safe  
✅ Suitable for interviewers, faculty, and GitHub viewers

Let me know if you want this in `.md` file format or want to add code samples, model accuracy results, or diagrams.
