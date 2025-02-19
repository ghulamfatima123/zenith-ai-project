# zenith_ai.py
from datetime import datetime
from config import model, logger

class ZenithAI:
    """
    ZenithAI provides mental health support, study plans, and career guidance
    using Google's Gemini Generative AI.
    """
    def __init__(self):
        self.mood_history = []   # List of mood check-in records
        self.task_history = []   # List of career exploration records
        self.study_stats = {}    # Dictionary to track study sessions by subject

    def get_mental_health_support(self, mood: str, situation: str) -> dict:
        """
        Generate supportive mental health advice based on user's mood and situation.
        """
        prompt = f"""
        As a supportive friend and mental health ally, respond to:
        Mood: {mood}
        Situation: {situation}
        
        Provide:
        1. Empathetic understanding response
        2. Three practical coping strategies
        3. A positive affirmation
        4. When to seek professional help if needed
        
        Respond in plain text with clear section headers, not JSON.
        """
        try:
            response = model.generate_content(prompt)
            logger.info("Mental health support generated successfully.")
            return {"text": response.text, "success": True}
        except Exception as e:
            logger.error("Error generating mental health support", exc_info=True)
            fallback_message = (
                "I'm having trouble connecting right now. "
                "Try these general coping strategies: deep breathing, taking a short walk, or writing your thoughts down. "
                "Remember: it's okay to not be okay, and seeking help is a sign of strength."
            )
            return {"text": fallback_message, "success": False}

    def create_study_plan(self, subject: str, goals: str, time_available: int) -> dict:
        """
        Generate a personalized study plan based on the subject, goals, and available study time.
        """
        prompt = f"""
        Create a Gen-Z friendly study plan for:
        Subject: {subject}
        Goals: {goals}
        Time Available: {time_available} hours

        Include:
        1. Break down of topics (list 3-5)
        2. Time allocation
        3. Study techniques (list 2-3)
        4. Break schedule
        5. Progress tracking metrics (list 2-3)
        
        Respond in plain text with clear section headers, not JSON.
        """
        try:
            response = model.generate_content(prompt)
            logger.info("Study plan generated successfully.")
            return {"text": response.text, "success": True}
        except Exception as e:
            logger.error("Error generating study plan", exc_info=True)
            fallback_message = (
                "I'm having difficulty creating your plan right now. "
                "Consider breaking your subject into 3-4 main topics, studying in 25-minute intervals with 5-minute breaks, "
                "and tracking progress by completing practice questions."
            )
            return {"text": fallback_message, "success": False}

    def career_guidance(self, interests: str, skills: str, values: str) -> dict:
        """
        Generate career guidance based on the user's interests, skills, and values.
        """
        prompt = f"""
        Provide Gen-Z focused career guidance based on:
        Interests: {interests}
        Skills: {skills}
        Values: {values}

        Include:
        1. Potential career paths (list 3-5)
        2. Required skills and education
        3. Growth opportunities
        4. Work-life balance considerations 
        5. Current industry trends

        Respond in plain text with clear section headers, not JSON.
        """
        try:
            response = model.generate_content(prompt)
            logger.info("Career guidance generated successfully.")
            return {"text": response.text, "success": True}
        except Exception as e:
            logger.error("Error generating career guidance", exc_info=True)
            fallback_message = (
                "I'm experiencing issues providing specific guidance. "
                "Consider researching careers that combine your interests and skills, looking at education requirements on job sites, "
                "and connecting with professionals in fields you're interested in."
            )
            return {"text": fallback_message, "success": False}
