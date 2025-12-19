🌾 Smart Farming Crop Recommendation System 🌱

An intelligent crop recommendation system using Machine Learning and a GUI demonstration for smart farming.

This project predicts the most suitable crop based on soil type, weather, irrigation, and fertilizer data. It demonstrates both data analysis using ML and a user-friendly GUI for farm recommendations.


---

🚀 Project Overview

The main goal of this project is to help farmers make informed decisions by predicting which crops are best suited for their land and environment.

Key Highlights:

Machine Learning-based crop prediction using Random Forest and Gradient Boosting.

Feature selection to identify the most influential soil and weather parameters.

Standalone Tkinter GUI for demonstration.

Dataset includes soil type, N-P-K content, temperature, rainfall, and irrigation factors.



---

📁 Repository Structure

Smart-Farming-Crop-Recommendation/
│
├── dataset/                     
│   └── Crop_recommendationV2_with_soil_fertilizer_irrigation.csv
│
├── ML_Analysis/                 
│   └── Crop_Analysis.ipynb      # ML model training & evaluation in Colab
│
├── GUI/                         
│   └── smart_farming_gui.py     # Tkinter GUI demo
│
├── screenshots/                 
│   ├── gui_demo.png             # Screenshot of GUI
│   └── ml_results.png           # ML model results / accuracy
│
├── README.md                    
└── requirements.txt              # Required Python packages


---

📊 ML Analysis

Models Used:

Random Forest Classifier 🌳

Gradient Boosting Classifier ⚡


Feature Selection: Top 8 important features selected using Random Forest importance.

Evaluation: Accuracy, classification report, and model comparison.


Example Accuracy Comparison:

Model	Accuracy

Random Forest 🌳	0.99
Gradient Boosting ⚡	0.97


> Screenshot of results available in ml_results.png




---

🖥️ GUI Demonstration

Built with Tkinter 

Rule-based crop recommendation for demo purposes

User inputs: Soil Type, Temperature, Rainfall

Outputs recommended crop


Example GUI Screenshot:




---

⚙️ Installation Instructions

1. Clone the repository:

$ git clone https://github.com/semwalanshika0405/Smart Farming Recommendation System


2. Install dependencies:

pip install -r requirements.txt


3. Run GUI:

Recommendation_System.py


---

🔮 Future Enhancements

Fertilizer recommendation based on soil analysis

Crop disease prediction module

Integration with real-time weather APIs

Web/mobile app version of the GUI



---

📄 Developed By -

    Anshika Semwal



Anshika Semwal
BCA (AI & DS) Student
