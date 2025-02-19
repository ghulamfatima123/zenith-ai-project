Below is a complete, ready-to-use `README.md` for your GitHub repository:

# Zenith: Your AI-Powered Personal Growth & Wellness Companion

Zenith is an interactive web application that provides personalized mental health support, custom study plans, and tailored career guidance using Google's Gemini Generative AI and Streamlit. It’s designed to help you navigate daily challenges, optimize your study routine, and explore career options—all in one intuitive platform.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Contact](#contact)

---

## Overview

Zenith combines the power of modern AI with a clean, interactive web interface to support your personal and professional growth. Whether you need a mental health check-in, a study plan breakdown, or insights into potential career paths, Zenith tailors its guidance to your unique situation.

---

## Features

- **Personalized Mental Health Support:**  
  Get compassionate advice and coping strategies based on your current mood and situation.
  
- **Custom Study Plans:**  
  Receive a detailed study plan that breaks down subjects into manageable topics, with time allocations and study techniques.

- **Tailored Career Guidance:**  
  Explore career paths that align with your interests, skills, and values, complete with insights on required skills and industry trends.

- **Progress Tracking:**  
  Monitor your mood check-ins, study sessions, and career explorations over time.

- **Robust Error Handling & Logging:**  
  Ensures a smooth user experience and easy debugging.

- **Modular & Clean Code:**  
  Organized into separate modules for configuration, business logic, and UI, following best practices.

---

## Tech Stack

- **Python 3.8+**
- **Streamlit:** For building the web interface.
- **Google Gemini AI:** For generating personalized content.
- **dotenv:** For managing environment variables.
- **Logging:** Python’s built-in logging module.

---

## Project Structure

```
zenith-ai-project/
├── config.py           # Handles environment variables, API configuration, and logging.
├── zenith_ai.py        # Contains the ZenithAI class with core business logic.
├── main.py             # The Streamlit UI and application entry point.
├── .env                # Environment variables (contains API keys; do not commit this).
├── .gitignore          # Specifies files/folders to ignore (e.g., .env).
├── README.md           # This documentation file.
└── requirements.txt    # Lists the project dependencies.
```

- **config.py:**  
  Loads environment variables and sets up the Gemini AI model along with logging.

- **zenith_ai.py:**  
  Implements the `ZenithAI` class that builds prompts, interacts with the AI, and handles responses.

- **main.py:**  
  Contains the UI logic using Streamlit, where users input their data and see the generated responses.

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/zenith-ai-project.git
   cd zenith-ai-project
   ```

2. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**

   Create a `.env` file in the project root and add your Gemini API key:
   
   ```env
   GEMINI_API_KEY=your_actual_api_key_here
   ```

5. **Ensure `.env` is in `.gitignore`:**

   Verify that your `.gitignore` file contains:
   
   ```gitignore
   .env
   ```

---

## Usage

1. **Run the Application:**

   ```bash
   streamlit run main.py
   ```

2. **Interact with Zenith:**

   - **Wellness Check-in:**  
     Select your current mood, enter a brief description of your situation, and receive supportive advice.
     
   - **Study Zone:**  
     Provide your subject and study goals to generate a personalized study plan.
     
   - **Career Explorer:**  
     Input your interests, skills, and values to receive tailored career guidance.
     
   - **Progress Tracker:**  
     View your mood history, study sessions, and career explorations.
     
---
##Contact
Email: fatimaghulam626@gmail.com
