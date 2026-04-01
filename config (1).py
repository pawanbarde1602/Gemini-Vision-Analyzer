"""
Configuration file for Gemini Vision App
Contains model configurations and analysis prompts
"""

# Available Gemini Models (ordered by recommendation)
GEMINI_MODELS = [
    "gemini-2.5-flash",              # Recommended: Best balance of speed and cost
    "gemini-2.0-flash",              # Fast and efficient
    "gemini-flash-latest",           # Latest flash model
    "gemini-flash-lite-latest",      # Lightest/cheapest option
    "gemini-2.5-pro",                # Most capable (higher cost)
    "gemini-pro-latest",             # Latest pro model
]

# Default model
DEFAULT_MODEL = "gemini-2.5-flash"

# Model descriptions
MODEL_DESCRIPTIONS = {
    "gemini-2.5-flash": "⚡ Recommended - Best balance of speed, quality, and cost",
    "gemini-2.0-flash": "⚡ Fast and efficient for quick analyses",
    "gemini-flash-latest": "⚡ Latest flash model with newest features",
    "gemini-flash-lite-latest": "💰 Most cost-effective option",
    "gemini-2.5-pro": "🎯 Highest quality analysis (premium pricing)",
    "gemini-pro-latest": "🎯 Latest pro model with advanced capabilities",
}

# Analysis Prompts
PROMPTS = {
    "description": """Analyze this image and provide a comprehensive description including:
    - Main subject and objects
    - Colors and visual elements
    - Setting and environment
    - Notable details and context
    - Overall mood or theme
    
    Provide a well-structured, detailed response.""",
    
    "ocr": """Perform OCR (Optical Character Recognition) on this image:
    1. Extract ALL visible text from the image
    2. Maintain the original structure and formatting where possible
    3. If there are multiple sections or columns, clearly separate them
    4. Note any text that is unclear or partially visible
    5. If no text is found, state that clearly
    
    Present the extracted text in a clean, readable format.""",
    
    "custom": "Analyze the image based on the following question or instruction:\n\n{prompt}\n\nProvide a detailed and relevant response."
}

# App Configuration
APP_CONFIG = {
    "title": "🔍 Gemini Vision Analyzer",
    "page_icon": "🔍",
    "layout": "wide",
    "sidebar_state": "expanded"
}

# Supported image formats
SUPPORTED_FORMATS = ["png", "jpg", "jpeg", "webp", "gif"]

# UI Messages
UI_MESSAGES = {
    "no_api_key": "⚠️ Please enter your Gemini API key in the sidebar to continue.",
    "no_image": "📸 Please upload an image to analyze.",
    "processing": "🔄 Analyzing image...",
    "success": "✅ Analysis complete!",
    "error": "❌ An error occurred during analysis.",
}
