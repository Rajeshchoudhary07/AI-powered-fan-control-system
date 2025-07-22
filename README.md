# AI-powered-fan-control-system


An **AI-powered fan control system** that predicts when to turn a fan **ON/OFF** based on historical usage patterns and real-time conditions, aiming to improve comfort and energy efficiency.

---

## 🔹 Key Features

- ✅ **Time-Based Predictions** – Suggests actions for morning, afternoon, and evening  
- ✅ **Confidence Scoring** – Displays model prediction confidence (e.g., 95%)  
- ✅ **Real-Time Status** – Shows current fan state and last toggled time  
- ✅ **Operation History** – Logs all ON/OFF events with timestamps  
- ✅ **Automated Control** – Auto-switches fan when prediction confidence is high  

---

## 🧠 Tech Stack

| Layer        | Technology                         |
|--------------|-------------------------------------|
| **Backend**  | Python, Scikit-learn, Pandas, Joblib |
| **Frontend** | Console-based UI *(Extendable to Web/Mobile)* |

---

## 📦 How It Works

1. Collects fan usage data over time (e.g., ON/OFF times and durations)
2. Trains a supervised ML model (e.g., Logistic Regression or Random Forest)
3. Predicts the optimal fan state for the current time/context
4. Displays real-time status and triggers auto-control when conditions match

---

## 📌 Use Cases

- 🏠 **Smart Homes** – Automates fan usage to save power  
- 🏢 **IoT Devices** – Seamlessly integrates into home automation setups  
- 📊 **Behavior Analysis** – Learns and adapts to user preferences over time  

---

## 🚀 Future Enhancements

- Web or mobile-based dashboard for remote access  
- Integration with smart home APIs (e.g., Alexa, Google Home)  
- Support for temperature and humidity sensor data  
- Battery backup and offline logging

---

## ⚠️ Disclaimer

This is a prototype project aimed at showcasing AI-assisted device control. Final deployments should include manual override options and safety checks.
