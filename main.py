# main.py
import streamlit as st
import random
from datetime import datetime
from zenith_ai import ZenithAI

def main():
    st.title("✨ Zenith")
    st.subheader("Your Personal Growth & Wellness Companion")
    st.write("Zenith is here to assist you with mental health support, career guidance, and study plans.")

    # Initialize or retrieve the ZenithAI instance in session state
    if "zenith" not in st.session_state:
        st.session_state.zenith = ZenithAI()

    # Sidebar Navigation
    page = st.sidebar.selectbox(
        "Choose Your Vibe",
        ["🧘‍♀️ Wellness Check-in", "📚 Study Zone", "💫 Career Explorer", "📊 Progress Tracker"]
    )

    # -------------------------------------------------------------------------
    # Wellness Check-in
    # -------------------------------------------------------------------------
    if page == "🧘‍♀️ Wellness Check-in":
        st.header("🌟 Daily Vibe Check")
        col1, col2 = st.columns(2)
        with col1:
            mood = st.select_slider(
                "How are you feeling right now?",
                options=["😔", "😕", "😐", "🙂", "😊"],
                value="😐"
            )
        with col2:
            situation = st.text_area("Share your thoughts:", placeholder="What's on your mind?")

        if st.button("Get Support 💭"):
            if not situation.strip():
                st.warning("Please share what's on your mind to receive support.")
            else:
                with st.spinner("Finding the perfect support for you..."):
                    support = st.session_state.zenith.get_mental_health_support(mood, situation)
                    if support["success"]:
                        st.markdown(support["text"])
                        note_preview = situation if len(situation) <= 50 else situation[:50] + "..."
                        st.session_state.zenith.mood_history.append({
                            "timestamp": datetime.now(),
                            "mood": mood,
                            "notes": note_preview
                        })
                    else:
                        st.warning(support["text"])

    # -------------------------------------------------------------------------
    # Study Zone
    # -------------------------------------------------------------------------
    elif page == "📚 Study Zone":
        st.header("📚 Study Zone")
        subject = st.text_input("What are you studying?")
        goals = st.text_area("What do you want to achieve?")
        time_available = st.number_input("Hours available for study:", min_value=1, max_value=8, value=2)

        if st.button("Create Study Plan 📝"):
            if not subject.strip() or not goals.strip():
                st.warning("Please provide both the subject and your study goals.")
            else:
                with st.spinner("Crafting your personalized study plan..."):
                    plan = st.session_state.zenith.create_study_plan(subject, goals, time_available)
                    if plan["success"]:
                        st.markdown(plan["text"])
                        st.session_state.zenith.study_stats[subject] = st.session_state.zenith.study_stats.get(subject, 0) + 1
                    else:
                        st.warning(plan["text"])

    # -------------------------------------------------------------------------
    # Career Explorer
    # -------------------------------------------------------------------------
    elif page == "💫 Career Explorer":
        st.header("💫 Career Explorer")
        interests = st.text_area("What are you passionate about?", placeholder="Art, technology, helping others...")
        skills = st.text_area("What are your strengths?", placeholder="Coding, writing, problem-solving...")
        values = st.text_area("What matters most to you in a career?", placeholder="Creativity, impact, flexibility...")

        if st.button("Explore Careers 🚀"):
            if not interests.strip() or not skills.strip():
                st.warning("Please provide both your interests and skills for accurate guidance.")
            else:
                with st.spinner("Discovering your perfect career paths..."):
                    guidance = st.session_state.zenith.career_guidance(interests, skills, values)
                    if guidance["success"]:
                        st.markdown(guidance["text"])
                        combined_content = (interests + " " + skills + " " + values).strip()
                        preview = combined_content if len(combined_content) <= 50 else combined_content[:50] + "..."
                        st.session_state.zenith.task_history.append({
                            "timestamp": datetime.now(),
                            "type": "career_exploration",
                            "content": preview
                        })
                    else:
                        st.warning(guidance["text"])

    # -------------------------------------------------------------------------
    # Progress Tracker
    # -------------------------------------------------------------------------
    elif page == "📊 Progress Tracker":
        st.header("📊 Your Journey")
        total_study_sessions = sum(st.session_state.zenith.study_stats.values())
        total_mood_checkins = len(st.session_state.zenith.mood_history)
        total_career_explorations = len(st.session_state.zenith.task_history)

        col1, col2, col3 = st.columns(3)
        col1.metric("Study Sessions", total_study_sessions)
        col2.metric("Mood Check-ins", total_mood_checkins)
        col3.metric("Career Explorations", total_career_explorations)

        if st.session_state.zenith.mood_history:
            st.subheader("Mood History")
            for entry in st.session_state.zenith.mood_history[-5:]:
                st.write(f"{entry['timestamp'].strftime('%Y-%m-%d %H:%M')} - {entry['mood']} - {entry['notes']}")
            
        if st.session_state.zenith.study_stats:
            st.subheader("Study Topics")
            for subj, count in st.session_state.zenith.study_stats.items():
                st.write(f"{subj}: {count} session{'s' if count > 1 else ''}")

#footer 
    st.markdown("---")
    motivational_quotes = [
        "✨ You've got this!",
        "🌟 Small steps, big impact",
        "💫 Your future is bright",
        "🚀 Keep growing, keep glowing",
        "🌱 Progress over perfection"
    ]
    st.markdown(f"### {random.choice(motivational_quotes)}")

if __name__ == "__main__":
    main()
