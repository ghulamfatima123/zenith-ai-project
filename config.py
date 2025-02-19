# config.py
import os
import logging
from dotenv import load_dotenv
import streamlit as st
import google.generativeai as genai

# Load environment variables from the .env file
load_dotenv()

# Get the API key from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("API key not found. Please set GEMINI_API_KEY in your .env file.")
    st.stop()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Configure the Gemini API using the API key
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-pro")
