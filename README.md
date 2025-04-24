# 🎓 StudyBuddy AI — Intelligent Study Planner & Academic Support Assistant

**StudyBuddy AI** is an expert system web app that provides personalized academic support and study planning assistance for students. It combines rule-based decision logic with Retrieval-Augmented Generation (RAG) to deliver intelligent, real-time suggestions based on user input. Built with Python and Streamlit, the app helps students enhance productivity, organize their study schedules, and overcome academic challenges.

🔗 **Live Demo (if deployed)**: *Add your Streamlit URL here*

---

## 🚀 Features

- 📅 Generates custom study plans based on user goals
- 💡 Provides dynamic learning strategies and productivity tips
- 🧠 Uses rule-based logic and RAG to understand free-text queries
- 📜 Includes a rich external knowledge base of study tips
- 🌐 Interactive UI with fast responses built using Streamlit

---

## 🧰 Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Logic Engine:** Rule-based expert system (`rules_engine.py`)
- **AI Query Handling:** Retrieval-Augmented Generation (`rag_engine.py`)
- **Data:** Knowledge base (`study_tips.txt`)
- **Deployment:** Streamlit Cloud or local

---

## 📁 Project Structure

```
StudyBuddy_Project/
├── app.py                   # Streamlit frontend logic
├── rules_engine.py          # Expert system rules for study planning
├── rag_engine.py            # RAG-based smart query handler
├── study_tips.txt           # Knowledge base for query retrieval
├── requirements.txt         # Python dependencies
├── FINAL_PROJECT_REPORT_ai2001.docx  # Academic report
└── README.md                # Project documentation
```

---

## 📦 Installation & Setup (Local)

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/StudyBuddyAI.git
   cd StudyBuddyAI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**:
   ```bash
   streamlit run app.py
   ```

---

## ✨ How It Works

### 🧠 Rule Engine (`rules_engine.py`)
Implements IF-THEN logic to deliver:
- Time management tips
- Subject prioritization
- Study style matching

Example rule:
```python
if user_input == "I have exams soon":
    return "Focus on creating a revision timetable with high-yield topics."
```

### 🔍 RAG Engine (`rag_engine.py`)
- Uses string similarity + keyword mapping to match free-text queries with curated tips
- Pulls from `study_tips.txt`, a file with motivational strategies, study hacks, and academic guides

---

## 📃 Sample Query Scenarios

- "I find it hard to stay focused"
- "Help me prepare for my math final"
- "Suggest a study plan for 3 subjects in 5 days"

---

## 📄 Final Report

See `FINAL_PROJECT_REPORT_ai2001.docx` for:
- Problem statement
- Architecture diagram
- Implementation details
- Limitations and future improvements

---

## 👤 Authors

- Renya Ann Regi – Frontend & Rule Design
- Rini Issac – Knowledge Base & RAG Logic
- Varsha Reghu – Documentation & Evaluation

---

## 📌 License

This project is licensed under the MIT License.

---

## ⚠️ Disclaimer

StudyBuddy AI is designed for academic support and should not replace professional academic advising. Suggestions are generated using rule-based logic and simplified NLP techniques for educational use.

