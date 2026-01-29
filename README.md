# ⚽ Football Match Analysis using Computer Vision

This project focuses on **automated football match analysis** using computer vision techniques.  
It detects and tracks players, referees, and the ball, differentiates teams based on appearance, identifies ball possession, and calculates **team-wise ball control statistics** from match footage.

---

## 🔍 Key Features

✅ **Team Differentiation**
- Players are grouped into teams using visual cues (jersey color / appearance)
- Each team is marked with a distinct color for easy identification

✅ **Player Detection & Tracking**
- Detects all players in the frame
- Maintains consistent tracking across frames

✅ **Referee Detection**
- Detects and marks the referee separately from players
- Helps avoid false team classification

✅ **Ball Detection & Tracking**
- Detects the football in each frame
- Tracks ball movement across the match

✅ **Ball Possession Identification**
- Identifies which player currently has control of the ball
- Highlights the **player in possession**

✅ **Team Ball Control Calculation**
- Calculates total ball possession time per team
- Outputs **team-wise ball control percentages**

---

## 🎥 Demo / Output Video

GitHub does not support direct video embedding, but you can view the project output on YouTube.

Click the image below to watch the demo:

[![Football Analysis Demo](https://img.youtu.be/vi/VhowC7ncxAE/0.jpg)](https://youtu.be/VhowC7ncxAE)

👉 Replace `YOUR_VIDEO_ID` with your actual YouTube video ID.

---

## 📁 Project Structure

```text
Football_analysis/
├── data/                 # Input match videos
├── src/                  # Source code (detection, tracking, logic)
├── results/              # Output videos / statistics
├── notebooks/            # Experiments and analysis
├── requirements.txt
├── .gitignore
└── README.md

