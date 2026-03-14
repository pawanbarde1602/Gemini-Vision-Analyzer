🔍 Gemini Vision Analyzer
Transform any image into actionable insights with the power of Google's Gemini AI

Upload • Analyze • Discover

✨ What is Gemini Vision Analyzer?
Gemini Vision Analyzer is a sleek, production-ready web application that harnesses Google's cutting-edge Gemini AI to analyze images instantly. Whether you need to describe a photo, extract text, detect objects, or get detailed insights — this tool does it all with just one click.

🚀 No coding required. Just upload and analyze!

✨ Features
📝 General Image Description
Get comprehensive analysis of your images including:

Main subjects and objects
Colors and visual elements
Setting and environment
Notable details and context
Overall mood and theme
📄 OCR Analysis
Extract text from images with high accuracy:

Extract all visible text
Maintain original formatting
Handle multiple columns/sections
Downloadable text output
💬 Custom Prompts
Ask specific questions about your images:

Flexible question interface
Contextual analysis
Detailed AI-powered responses
🚀 Quick Start
Prerequisites
Python 3.8 or higher
Google Gemini API key (Get one here)
Installation
Clone or download this repository
git clone <your-repo-url>
cd gemini-vision-app
Install dependencies
pip install -r requirements.txt
Configure API Key
Create a .env file in the project root:

cp .env.example .env
Edit the .env file and add your Gemini API key:

GEMINI_API_KEY=your_actual_api_key_here
Get your API key: Visit Google AI Studio

Run the application
streamlit run app.py
Start analyzing images!
The app will open in your browser
Upload images and select analysis features
🔑 Getting Your API Key
Visit Google AI Studio
Sign in with your Google account
Create a new API key or use an existing one
Copy the key and paste it in the app's sidebar
Note: Your API key is stored only in your browser session and is never saved to disk.

🤖 Available Models
The app supports multiple Gemini models with different capabilities:

Model	Description	Best For
gemini-2.5-flash ⭐	Recommended - Best balance	Most use cases
gemini-2.0-flash	Fast and efficient	Quick analyses
gemini-flash-latest	Latest flash features	New capabilities
gemini-flash-lite-latest	Most cost-effective	Budget-conscious
gemini-2.5-pro	Highest quality	Complex analysis
gemini-pro-latest	Latest pro features	Advanced needs
Default: gemini-2.5-flash (recommended for best cost/performance ratio)

📖 How to Use
Launch the app

streamlit run app.py
Upload an image

Click "Browse files" or drag & drop
Supported formats: PNG, JPG, JPEG, WEBP, GIF
Choose a feature

General Description: Click "Analyze Image"
OCR Analysis: Click "Extract Text"
Custom Prompt: Enter your question and click "Ask Question"
View results

Results appear in a formatted display
OCR results can be downloaded as TXT files
📁 Project Structure
gemini-vision-app/
├── app.py              # Main Streamlit application
├── config.py           # Configuration and prompts
├── requirements.txt    # Python dependencies
├── .env.example        # Environment variable template
├── .gitignore         # Git ignore rules
└── README.md          # This file
🎨 Features Highlights
Professional UI: Modern dark theme with gradient accents
Responsive Design: Works on desktop and mobile browsers
Easy API Management: Simple sidebar configuration
Model Flexibility: Choose from multiple Gemini models
Download Results: Export OCR text as files
Error Handling: Clear error messages and guidance
Session Management: API key persists during session
💡 Use Cases
📸 Content Creators — Generate captions and descriptions for social media
🔬 Researchers — Analyze scientific images and diagrams
📚 Students — Extract text from handwritten notes or slides
🛒 E-commerce — Auto-generate product descriptions from photos
🏢 Businesses — Digitize documents and receipts with OCR
🎨 Designers — Get color analysis and composition feedback
🛡️ Security
✅ Your API key is stored locally in .env file ✅ Never committed to GitHub (protected by .gitignore) ✅ No data stored on external servers

📋 Requirements
Python 3.8+
Google Gemini API key (free tier available)
🤝 Contributing
Feel free to fork, improve, and submit pull requests!

📄 License
MIT License — Free to use, modify, and distribute.

