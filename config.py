# # config.py
# import os
# import logging
# from dotenv import load_dotenv
# import streamlit as st
# import google.generativeai as genai

# # Load environment variables from the .env file
# load_dotenv()

# # Get the API key from environment variables
# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     st.error("API key not found. Please set GEMINI_API_KEY in your .env file.")
#     st.stop()

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[logging.StreamHandler()]
# )
# logger = logging.getLogger(__name__)

# # Configure the Gemini API using the API key
# genai.configure(api_key=api_key)
# model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
# config.py
import os
import logging
import openai
from dotenv import load_dotenv

# Load .env (so OPENAI_API_KEY can be pulled from there, if you’ve set it)
load_dotenv()

# ─── OpenRouter / OpenAI Configuration ──────────────────────────────────────
# Your OpenRouter API key should be in an environment variable named OPENAI_API_KEY
openai.api_key = os.getenv("OPENAI_API_KEY") or ""
openai.api_base = "https://openrouter.ai/api/v1"

# ─── Logger Setup ────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger("zenithai")

# If someone forgot to set the key, we log an error and (optionally) stop the app.
if not openai.api_key:
    logger.error("OPENAI_API_KEY not found in environment. Please set it in your .env or system environment.")
