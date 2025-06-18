import streamlit as st

st.set_page_config(page_title="Sai Kumar Resume", layout="wide")

# Header
st.title("Sai Kumar Golla")
st.write("📧 gollasaikumar8888@gmail.com | 📱 +91-6281255873")
st.write("[LinkedIn](https://www.linkedin.com/in/golla-saikumar-4a4059352)")

# Objective
st.header("🎯 Objective")
st.write(
    "Aspiring AI & ML Engineer with a strong foundation in Python, Java, and Data Structures & Algorithms. "
    "Passionate about solving complex problems through AI-driven solutions and innovative technology."
)

# Education
st.header("📘 Education")
st.markdown("""
- **B.Tech in Computer Science (AI & ML)**, Malla Reddy College of Engineering and Technology, 2024–Present – **CPI: 7.60**
- **Diploma in Mechanical Engineering**, Sri Sangameswara Govt Polytechnic College, 2024 – **CPI: 6.10**
- **SSC**, Kakatiya High School, 2021 – **GPA: 10.0**
""")

# Skills
st.header("🛠️ Technical Skills")
st.markdown("""
- **Languages:** Python, Java  
- **Web Technologies:** HTML, CSS  
- **Database:** MySQL  
- **AI/ML:** Generative AI, ML Algorithms  
- **Tools & Platforms:** Google Cloud, VS Code  
- **Soft Skills:** Problem-Solving, Communication  
- **Competitive Programming:** Active Python user on HackerRank
""")

# Project
st.header("🚀 Projects")
st.markdown("""
- **College Chatbot**: Built using NLP and Machine Learning algorithms to facilitate student-college interaction.
""")

# Certifications
st.header("📜 Certifications & Workshops")
st.markdown("""
- *AI for Beginners* – HP LIFE Online Course  
- *Machine Learning* – (Platform not specified)
""")

# Footer
st.markdown("---")
st.caption("Generated using Streamlit")
