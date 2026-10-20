AI Data Analytics Dashboard
A web-based data analytics platform with AI predictions, interactive visualizations, and smart chatbot features.

Features

CSV File Upload: Easy drag-and-drop CSV file uploading

Data Visualizations: Line charts, bar charts, 3D scatter plots

AI Predictions: Linear Regression model for forecasting next values

Smart Chatbot: Query data with natural language (highest, lowest, trend, summary, anomaly)

Voice Input: Speak your questions using voice recognition

PDF Reports: Generate professional PDF reports automatically

Theme Customization: Neon, Dark, and Light themes

Quick Start
Installation

Bash
# Clone repository
git clone https://github.com/yourusername/ai-data-analytics-dashboard.git
cd ai-data-analytics-dashboard

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
The app will open at http://localhost:8501

How to Use
Upload CSV File

Click "Upload CSV" in sidebar

Select your CSV file (drag & drop or click to browse)

Configure Analysis

Select number of rows (5-30)

Choose column to analyze from dropdown

Pick theme (Neon/Dark/Light)

View Analytics (Analytics Tab)

Data table preview

Line chart trend analysis

Bar chart visualization

3D interactive scatter plot

AI prediction for next value

Ask Questions (Chatbot Tab)

Use quick suggestion buttons

Type custom questions

Use voice input (speak your question)

Get instant data insights

Download Report (Report Tab)

Click "Generate Report"

Download PDF with analysis summary

Technologies Used

Backend: Python 3.8+

Framework: Streamlit

Data Processing: Pandas, NumPy

Visualization: Matplotlib, Plotly

Machine Learning: Scikit-learn (Linear Regression)

Voice Processing: SpeechRecognition

PDF Generation: ReportLab

Project Structure

Plaintext
ai-data-analytics-dashboard/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── sample_data.csv                 # Sample dataset for testing
├── README.md                       # This file
├── .gitignore                      # Git ignore configuration
│
└── AI_Data_Analytics_Dashboard_Report.docx   # Project documentation
Dependencies
All required packages are listed in requirements.txt:

streamlit1.28.0
pandas2.0.0
numpy1.24.0
matplotlib3.7.0
plotly5.14.0
scikit-learn1.3.0
SpeechRecognition3.10.0
pyaudio0.2.13
reportlab==4.0.4

System Architecture
6 Core Modules:

User Interface Module: Streamlit-based interactive dashboard

Data Processing Module: CSV handling and data validation

Visualization Module: Chart and graph generation

Machine Learning Module: Predictive analytics using Linear Regression

AI Chatbot Module: Natural language query processing

Report Generator Module: PDF report creation

Chatbot Queries
Ask any of these questions to the chatbot:

"What is the highest value?" - Returns maximum value

"What is the lowest value?" - Returns minimum value

"Show me the trend" - Indicates if data is going up or down

"Give me a summary" - Shows statistical summary

"Check for anomalies" - Detects unusual data points

Themes
Three beautiful themes available:

Neon: Dark blue background with cyan and purple accents

Dark: Pure black with subtle gradients

Light: White background with blue accents

How AI Predictions Work
The system uses Linear Regression to predict the next value in your dataset:

Trains model on existing data

Learns the trend/pattern

Predicts the next value based on learned pattern

Shows prediction confidence

Sample Usage

Python
# Upload sample_data.csv
# Select "Value" column
# See automatic analysis, charts, and prediction
# Ask chatbot: "What is the highest value?"
# Download PDF report
Configuration

Adjust data rows: Sidebar slider allows filtering 5-30 rows from your dataset

Change themes: Select from Neon, Dark, or Light in sidebar

Column selection: Only numeric columns are available for analysis

Output Examples

Charts: Line, Bar, 3D Scatter visualizations

Statistics: Mean, Max, Min, Standard Deviation

Predictions: Next value forecast using ML

Insights: Trend analysis, anomaly detection

Reports: Professional PDF with all analysis

Troubleshooting

Issue: "No numeric column found"

Ensure CSV has at least one numeric column

Check data types in your file

Issue: Voice input not working

Ensure microphone is connected

Check audio permissions

SpeechRecognition may need internet connection

Issue: 3D plot not displaying

Requires updated browser

Check Plotly installation: pip install --upgrade plotly

Learning Resources

Streamlit Docs: https://docs.streamlit.io

Scikit-learn: https://scikit-learn.org

Pandas: https://pandas.pydata.org

Plotly: https://plotly.com

Author
Suranjan Gaur
