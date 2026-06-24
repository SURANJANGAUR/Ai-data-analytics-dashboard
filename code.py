
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import speech_recognition as sr
from sklearn.linear_model import LinearRegression
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


# ===== PAGE CONFIGURATION =====
st.set_page_config(page_title="AI Data Analytics Dashboard", layout="wide")

st.title("📊 AI Data Analytics Dashboard")


# ===== THEME SELECTION =====
theme = st.sidebar.selectbox("🎨 Theme", ["Neon", "Dark", "Light"])

if theme == "Neon":
    bg = "linear-gradient(-45deg, #0f172a, #1e1b4b, #0ea5e9, #0f172a)"
elif theme == "Dark":
    bg = "linear-gradient(-45deg, #000000, #111827, #1f2937, #000000)"
else:
    bg = "linear-gradient(-45deg, #ffffff, #e5e7eb, #cbd5e1, #ffffff)"

st.markdown(f"""
<style>
.stApp {{
    background: {bg};
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: white;
}}

@keyframes gradientBG {{
    0% {{background-position: 0% 50%;}}
    50% {{background-position: 100% 50%;}}
    100% {{background-position: 0% 50%;}}
}}

.stButton>button {{
    width: 100%;
    border-radius: 10px;
    background: linear-gradient(90deg,#00ffe5,#7c3aed);
    color: black;
    font-weight: bold;
}}
</style>
""", unsafe_allow_html=True)


# ===== CHATBOT FUNCTION =====
def bot(q, df, col):
    """Process chatbot queries"""
    q = q.lower()

    if "highest" in q:
        return f"Highest value: {df[col].max()}"

    elif "lowest" in q:
        return f"Lowest value: {df[col].min()}"

    elif "trend" in q:
        return "UP 📈" if df[col].iloc[-1] > df[col].iloc[0] else "DOWN 📉"

    elif "summary" in q:
        return df.describe().to_string()

    elif "anomaly" in q:
        return "YES ⚠ anomaly detected" if df[col].std() > df[col].mean() * 0.5 else "NO clean data"

    else:
        return "Try: highest, lowest, trend, summary, anomaly"


# ===== VOICE INPUT FUNCTION =====
def voice_to_text():
    """Convert voice to text"""
    r = sr.Recognizer()

    with sr.Microphone() as source:
        st.info("🎤 Listening...")
        audio = r.listen(source)

    try:
        return r.recognize_google(audio)
    except:
        return ""


# ===== FILE UPLOAD =====
file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

if file:

    df = pd.read_csv(file)

    rows = st.sidebar.slider("Rows", 5, len(df), 30)
    df = df.head(rows)

    num_cols = df.select_dtypes(include=np.number).columns.tolist()

    if len(num_cols) == 0:
        st.error("No numeric column found")
        st.stop()

    # Column selector
    col = st.sidebar.selectbox("📊 Select Column", num_cols)


    # ===== TABS =====
    tab1, tab2, tab3 = st.tabs(["📊 Analytics", "🤖 Chatbot", "📄 Report"])


    # ===== TAB 1: ANALYTICS =====
    with tab1:

        st.subheader(f"Analyzing Column: {col}")
        st.dataframe(df)

        # Line Chart
        st.line_chart(df[col])
        
        # Bar Chart
        st.bar_chart(df[col])

        # 3D Visualization
        st.subheader("🛰 3D Visualization")
        fig3d = px.scatter_3d(
            df,
            x=df.index,
            y=df[col],
            z=df[col],
            color=df[col]
        )
        st.plotly_chart(fig3d)

        # AI Prediction
        x = np.array(range(len(df[col]))).reshape(-1, 1)
        y = df[col].values

        model = LinearRegression()
        model.fit(x, y)

        pred = model.predict([[len(df)]])

        st.success(f"🤖 Next Prediction: {round(pred[0],2)}")


    # ===== TAB 2: CHATBOT =====
    with tab2:

        st.subheader("🤖 Smart Chatbot")

        if "voice_text" not in st.session_state:
            st.session_state.voice_text = ""

        # Voice Button
        if st.button("🎙 Speak Question"):
            text = voice_to_text()

            if text:
                st.session_state.voice_text = text
                st.success("You said: " + text)
            else:
                st.error("Could not understand voice")

        # Quick Suggestions
        st.write("💡 Quick Suggestions:")

        suggestions = ["highest", "lowest", "trend", "summary", "anomaly"]

        cols = st.columns(len(suggestions))

        clicked = ""
        for i, s in enumerate(suggestions):
            if cols[i].button(s):
                clicked = s

        # Text Input
        typed = st.text_input(
            "Ask your question",
            value=st.session_state.voice_text if st.session_state.voice_text else clicked
        )

        if typed:
            st.success(bot(typed, df, col))


    # ===== TAB 3: REPORT =====
    with tab3:

        st.subheader("📊 Report Generation")

        if st.button("Generate Report"):

            doc = SimpleDocTemplate("AI_Report.pdf")
            styles = getSampleStyleSheet()

            elements = [
                Paragraph("AI Data Analytics Report", styles["Title"]),
                Spacer(1, 12),
                Paragraph(f"Mean: {df[col].mean()}", styles["BodyText"]),
                Paragraph(f"Max: {df[col].max()}", styles["BodyText"]),
                Paragraph(f"Min: {df[col].min()}", styles["BodyText"]),
            ]

            doc.build(elements)

            with open("AI_Report.pdf", "rb") as f:
                st.download_button("⬇ Download Report", f, file_name="report.pdf")

else:
    st.info("⬅ Upload CSV file to start analysis")
