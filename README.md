# 🏏 Cricket Runs and Match Winner Prediction using Machine Learning & Neural Networks

This project predicts:
1. **Total Runs in a Cricket Match (First Innings)**
2. **Winning Team of the Match**

The models are trained using past ODI match data and deployed as a simple web application using **Streamlit**.

---

## 📁 Project Files

| File Name                | Purpose                                                           |
|--------------------------|-------------------------------------------------------------------|
| `app.py`                 | Main Streamlit app to predict runs and winner                    |
| `label_encoders.pkl`     | Stores label encoders for input transformation                   |
| `merged_odi_data.csv`    | Combined dataset of all matches used for model training          |
| `neural_network_runs.h5` | Neural network model for runs prediction                         |
| `odi_Batting_Card.csv`   | Player-wise batting data                                         |
| `odi_Bowling_Card.csv`   | Player-wise bowling data                                         |
| `odi_Fow_Card.csv`       | Fall of wickets data                                             |
| `odi_Matches_Data.csv`   | Main match-level data                                            |
| `players_info.csv`       | Player profiles and basic info                                   |
| `r&w.ipynb`              | Notebook file used for building and training models              |
| `scaler_run.pkl`         | Scaler object for runs prediction input                          |
| `scaler_winner.pkl`      | Scaler object for winner prediction input                        |
| `requirements.txt`       | List of Python libraries required to run this project            |

---

## 🔍 Project Features

- Predict **first innings runs** using historical data and match info.
- Predict **winning team** based on match conditions and first innings score.
- Clean and interactive **Streamlit web app** for users.
- Uses both **Machine Learning** and **Deep Learning** models.

---

## 🧪 Technologies Used

- Python
- Pandas, NumPy
- Scikit-learn
- XGBoost
- TensorFlow / Keras
- Streamlit

---

## ▶️ How to Run the Project Locally

### Step 1: Clone the repository

```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Step 2: Install the required libraries
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Run the Streamlit app
bash
Copy
Edit
streamlit run app.py
✅ Inputs You Provide in the Web App
Batting team

Bowling team

Venue

Overs completed

Wickets fallen

Toss winner

First innings total

🎯 Output You Get
Predicted Runs (during first innings)

Predicted Winning Team

📌 Note
This project is for academic and learning purposes only.

No personal or confidential data is included.

All files like .h5, .pkl, and .csv are part of the project folder and required for predictions.

📃 License
This project is open-source and free to use for educational purposes.

yaml
Copy
Edit

---

### 🟢 Next Steps

1. **Create a file** in your folder called `README.md`.
2. **Paste the above content** into that file.
3. If you're uploading to GitHub:
   - Add the file → Commit → Push to your GitHub repository.
