import streamlit as st
from rules_engine import generate_schedule
from rag_engine import StudyTipRetriever

st.set_page_config(page_title="StudyBuddy AI", layout="centered")
st.title("📚 StudyBuddy AI")
st.write("Your Intelligent Study Planner and Academic Support Assistant")

# --- Sidebar Inputs ---
st.sidebar.header("📝 Enter Your Study Details")
subject_list = []
for i in range(3):
    name = st.sidebar.text_input(f"Subject {i+1} Name", key=f"name_{i}")
    confidence = st.sidebar.selectbox(f"{name or 'Subject'} Confidence", ['low', 'medium', 'high'], key=f"conf_{i}")
    exam_days_left = st.sidebar.slider(f"Days until exam", 1, 30, key=f"days_{i}")
    if name:
        subject_list.append({'name': name, 'confidence': confidence, 'exam_days_left': exam_days_left, 'day': f'Day {i+1}'})

# --- Generate Study Plan ---
if st.sidebar.button("✅ Generate Study Plan"):
    if subject_list:
        schedule = generate_schedule(subject_list)
        st.subheader("🗓️ Your Personalized Study Plan")
        for item in schedule:
            st.markdown(f"📘 **{item['day']} → {item['subject']}**: {item['hours']} hrs")
    else:
        st.warning("Please enter at least one subject.")

# --- Academic Tips with RAG ---
st.markdown("---")
st.subheader("🤖 Ask StudyBuddy for a Study Tip")

query = st.text_input("Ask a question (e.g., How to avoid procrastination?)")

if query:
    try:
        retriever = StudyTipRetriever("data/study_tips.txt")
        answer = retriever.get_tip(query)
        st.success(f"🧠 {answer}")
    except Exception as e:
        st.error(f"❌ Error: {e}")
