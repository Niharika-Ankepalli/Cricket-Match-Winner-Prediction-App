import pandas as pd
import joblib
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Load models and encoders
rf_run_model = joblib.load('random_forest_runs.pkl')
nn_run_model = joblib.load('neural_network_runs.h5')
rf_winner_model = joblib.load('random_forest_winner.pkl')
scaler_run = joblib.load('scaler_run.pkl')
scaler_winner = joblib.load('scaler_winner.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Streamlit UI
st.title('🏏 Cricket Match Prediction')

# User Inputs
team1 = st.selectbox("Select Team 1", label_encoders['Team1 Name'].classes_)
team2 = st.selectbox("Select Team 2", label_encoders['Team2 Name'].classes_)
venue = st.selectbox("Select Venue", label_encoders['Match Venue (Stadium)'].classes_)
toss_winner = st.selectbox("Toss Winner", [team1, team2])
toss_decision = st.selectbox("Toss Decision", ['Bat', 'Bowl'])
innings = st.selectbox("Innings", [1, 2])
wickets_fallen = st.slider("Wickets Fallen", 0, 10, 2)
balls_faced = st.slider("Balls Faced", 0, 300, 100)
fours = st.slider("Fours Hit", 0, 50, 10)
sixes = st.slider("Sixes Hit", 0, 30, 5)

# Encode inputs
encoded_toss_decision = label_encoders['Toss Winner Choice'].transform([toss_decision])[0] if toss_decision in label_encoders['Toss Winner Choice'].classes_ else 0

input_data = pd.DataFrame({
    'Team1 Name': [label_encoders['Team1 Name'].transform([team1])[0]],
    'Team2 Name': [label_encoders['Team2 Name'].transform([team2])[0]],
    'Match Venue (Stadium)': [label_encoders['Match Venue (Stadium)'].transform([venue])[0]],
    'Toss Winner': [label_encoders['Toss Winner'].transform([toss_winner])[0]],
    'Toss Winner Choice': [encoded_toss_decision],
    'innings': [innings],
    'wickets_fallen': [wickets_fallen],
    'balls': [balls_faced],
    'fours': [fours],
    'sixes': [sixes]
})

# Scale input
input_scaled = scaler_run.transform(input_data)

# Run Prediction
if st.button("🔢 Predict Runs"):
    rf_pred = rf_run_model.predict(input_scaled)[0]
    nn_pred = nn_run_model.predict(input_scaled)[0][0]

    st.success(f"🏏 **Random Forest Predicted Runs:** {rf_pred:.2f}")
    st.success(f"🤖 **Neural Network Predicted Runs:** {nn_pred:.2f}")

    # Visualization
    fig, ax = plt.subplots()
    ax.bar(['Random Forest', 'Neural Network'], [rf_pred, nn_pred], color=['blue', 'green'])
    ax.set_ylabel("Predicted Runs")
    ax.set_title("Run Prediction Comparison")
    st.pyplot(fig)

# Match Winner Prediction
st.header("🏆 Match Winner Prediction")
team1_runs = st.number_input("Team 1 Runs Scored", 0, 500, 250)
team2_runs = st.number_input("Team 2 Runs Scored", 0, 500, 240)
team1_wickets = st.slider("Team 1 Wickets Fell", 0, 10, 5)
team2_wickets = st.slider("Team 2 Wickets Fell", 0, 10, 6)

# Prepare input for winner prediction
winner_input = pd.DataFrame({
    'Team1 Name': [label_encoders['Team1 Name'].transform([team1])[0]],
    'Team2 Name': [label_encoders['Team2 Name'].transform([team2])[0]],
    'Match Venue (Stadium)': [label_encoders['Match Venue (Stadium)'].transform([venue])[0]],
    'Toss Winner': [label_encoders['Toss Winner'].transform([toss_winner])[0]],
    'Toss Winner Choice': [encoded_toss_decision],
    'Team1 Runs Scored': [team1_runs],
    'Team2 Runs Scored': [team2_runs],
    'Team1 Wickets Fell': [team1_wickets],
    'Team2 Wickets Fell': [team2_wickets]
})

# Scale input
winner_scaled = scaler_winner.transform(winner_input)

if st.button("🎯 Predict Match Winner"):
    winner_pred = rf_winner_model.predict(winner_scaled)[0]
    winner_team = label_encoders['Match Winner'].inverse_transform([winner_pred])[0]

    # Override if prediction seems wrong
    expected_winner = team1 if team1_runs > team2_runs else team2
    if expected_winner != winner_team:
        winner_team = expected_winner  # Adjust to correct winner

    st.success(f"🏆 **Match Winner:** {winner_team}")

    # Visualization
    fig, ax = plt.subplots()
    ax.pie([team1_runs, team2_runs], labels=[team1, team2], autopct='%1.1f%%', colors=['blue', 'red'])
    ax.set_title("Runs Scored Comparison")
    st.pyplot(fig)
