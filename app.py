"""
Gemini Vision Analyzer - Streamlit App
A professional image analysis application using Google's Gemini Vision API
"""

import streamlit as st
import google.generativeai as genai
from PIL import Image
import io
import os
from pathlib import Path
from dotenv import load_dotenv
from config import (
    GEMINI_MODELS, DEFAULT_MODEL, MODEL_DESCRIPTIONS,
    PROMPTS, APP_CONFIG, SUPPORTED_FORMATS, UI_MESSAGES
)

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title=APP_CONFIG["title"],
    page_icon=APP_CONFIG["page_icon"],
    layout=APP_CONFIG["layout"],
    initial_sidebar_state=APP_CONFIG["sidebar_state"]
)

# Custom CSS for professional styling
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #FF6B35;
        --secondary-color: #004E89;
        --background-dark: #1E1E1E;
        --card-bg: #2D2D2D;
        --text-primary: #FFFFFF;
        --text-secondary: #B0B0B0;
        --success-color: #00C851;
        --warning-color: #FFB700;
        --error-color: #FF4444;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 10px;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
    }
    
    .main-header h1 {
        color: white;
        font-size: 2.5rem;
        margin-bottom: 0.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        color: rgba(255, 255, 255, 0.9);
        font-size: 1.1rem;
        margin: 0;
    }
    
    /* Feature cards */
    .feature-card {
        background: linear-gradient(145deg, #2d2d2d, #3a3a3a);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    
    .feature-card h3 {
        color: #667eea;
        margin-top: 0;
    }
    
    /* Result container */
    .result-container {
        background: #2d2d2d;
        padding: 1.5rem;
        border-radius: 10px;
        border: 1px solid #444;
        margin-top: 1rem;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1e1e1e 0%, #2d2d2d 100%);
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        border-radius: 8px;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background-color: #1e1e1e;
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #2d2d2d;
        border-radius: 8px;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        color: #b0b0b0;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    /* Info boxes */
    .info-box {
        background: linear-gradient(135deg, #667eea15, #764ba215);
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 6px;
        margin: 1rem 0;
    }
    
    /* Image container */
    .image-container {
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        margin: 1rem 0;
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #666;
        border-top: 1px solid #333;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Configure API key from environment
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Sidebar
with st.sidebar:
    # Model selection
    st.markdown("### 🤖 Model Selection")
    selected_model = st.selectbox(
        "Choose Model",
        options=GEMINI_MODELS,
        index=0,
        format_func=lambda x: f"{x}",
        help="Select the Gemini model to use for analysis"
    )
    
    # Show model description
    if selected_model in MODEL_DESCRIPTIONS:
        st.info(MODEL_DESCRIPTIONS[selected_model])
    
    st.markdown("---")
    
    # Model info
    with st.expander("ℹ️ About Models"):
        st.markdown("""
        **Flash Models** (Recommended):
        - Fast responses
        - Cost-effective
        - Great for most tasks
        
        **Pro Models**:
        - Highest quality
        - Complex analysis
        - Premium pricing
        """)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🔍 Gemini Vision Analyzer</h1>
    <p>Advanced image analysis powered by Google Gemini AI</p>
</div>
""", unsafe_allow_html=True)

# Check if API key is configured
if not api_key:
    st.error("⚠️ API key not configured. Please contact the administrator.")
    st.stop()

# Image upload section
st.markdown("### 📸 Upload Image")
uploaded_file = st.file_uploader(
    "Choose an image file",
    type=SUPPORTED_FORMATS,
    help=f"Supported formats: {', '.join(SUPPORTED_FORMATS).upper()}"
)

if uploaded_file:
    # Display uploaded image
    image = Image.open(uploaded_file)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="image-container">', unsafe_allow_html=True)
        st.image(image, caption="Uploaded Image", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Image info
    st.markdown(f"""
    <div class="info-box">
        📊 <strong>Image Info:</strong> {image.size[0]} × {image.size[1]} pixels | 
        Format: {image.format} | Mode: {image.mode}
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Analysis tabs
    st.markdown("### 🔍 Analysis Features")
    
    tab1, tab2, tab3 = st.tabs([
        "📝 General Description",
        "📄 OCR Analysis",
        "💬 Custom Prompt"
    ])
    
    # Initialize model
    model = genai.GenerativeModel(selected_model)
    
    # Tab 1: General Description
    with tab1:
        st.markdown("""
        <div class="feature-card">
            <h3>📝 General Image Description</h3>
            <p>Get a comprehensive analysis of your image including objects, colors, setting, and context.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("🔍 Analyze Image", key="desc_btn"):
            with st.spinner(UI_MESSAGES["processing"]):
                try:
                    response = model.generate_content([PROMPTS["description"], image])
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("#### 📊 Analysis Result")
                    st.markdown(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.success(UI_MESSAGES["success"])
                except Exception as e:
                    st.error(f"{UI_MESSAGES['error']} {str(e)}")
    
    # Tab 2: OCR Analysis
    with tab2:
        st.markdown("""
        <div class="feature-card">
            <h3>📄 OCR Text Extraction</h3>
            <p>Extract all visible text from your image with accurate optical character recognition.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("📄 Extract Text", key="ocr_btn"):
            with st.spinner(UI_MESSAGES["processing"]):
                try:
                    response = model.generate_content([PROMPTS["ocr"], image])
                    st.markdown('<div class="result-container">', unsafe_allow_html=True)
                    st.markdown("#### 📝 Extracted Text")
                    st.markdown(response.text)
                    st.markdown('</div>', unsafe_allow_html=True)
                    st.success(UI_MESSAGES["success"])
                    
                    # Download button for extracted text
                    st.download_button(
                        label="💾 Download as TXT",
                        data=response.text,
                        file_name="extracted_text.txt",
                        mime="text/plain"
                    )
                except Exception as e:
                    st.error(f"{UI_MESSAGES['error']} {str(e)}")
    
    # Tab 3: Custom Prompt
    with tab3:
        st.markdown("""
        <div class="feature-card">
            <h3>💬 Custom Question</h3>
            <p>Ask any specific question about your image and get detailed answers.</p>
        </div>
        """, unsafe_allow_html=True)
        
        custom_prompt = st.text_area(
            "Your Question",
            placeholder="e.g., What colors are dominant in this image? What emotion does it convey?",
            height=100,
            help="Enter any question or instruction related to the image"
        )
        
        if st.button("💬 Ask Question", key="custom_btn"):
            if custom_prompt.strip():
                with st.spinner(UI_MESSAGES["processing"]):
                    try:
                        formatted_prompt = PROMPTS["custom"].format(prompt=custom_prompt)
                        response = model.generate_content([formatted_prompt, image])
                        st.markdown('<div class="result-container">', unsafe_allow_html=True)
                        st.markdown("#### 💡 Response")
                        st.markdown(response.text)
                        st.markdown('</div>', unsafe_allow_html=True)
                        st.success(UI_MESSAGES["success"])
                    except Exception as e:
                        st.error(f"{UI_MESSAGES['error']} {str(e)}")
            else:
                st.warning("⚠️ Please enter a question or prompt.")

else:
    st.info(UI_MESSAGES["no_image"])
    st.markdown("""
    <div class="info-box">
        <h4>💡 What You Can Do</h4>
        <ul>
            <li><strong>📝 General Description:</strong> Get detailed analysis of image content, objects, and context</li>
            <li><strong>📄 OCR Analysis:</strong> Extract and read all text present in your images</li>
            <li><strong>💬 Custom Questions:</strong> Ask specific questions about your image</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p style="font-size: 1.1rem; font-weight: 600; color: #667eea;">Developed with ❤️ by Shivam Kumar Yadav</p>
    <p style="font-size: 0.9rem; color: #888; margin-top: 0.5rem;">🔍 Gemini Vision Analyzer | Powered by Google Gemini AI</p>
</div>
""", unsafe_allow_html=True)
