🏋️ AI Health Assistant

<p align="center">
  <strong>Personal Health Assistance & Diet Recommendation Agent</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/RAG-FAISS-00A67E?style=for-the-badge">
  <img src="https://img.shields.io/badge/AI-Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black">
  <img src="https://img.shields.io/badge/LangChain-RAG-1C3C3C?style=for-the-badge">
</p>

<p align="center">
  An AI-powered Streamlit application that combines health calculations, nutrition knowledge retrieval, and generative AI to create personalized diet recommendations and answer health-related questions.
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-how-it-works">How It Works</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-project-structure">Project Structure</a>
</p>

🌟 About the Project

AI Health Assistant is a Python and Streamlit project built around Retrieval-Augmented Generation (RAG).

The application collects basic user information such as age, gender, height, weight, activity level, fitness goal, diet type, and allergies. It then calculates BMI, BMR, TDEE, and an estimated calorie target.

For AI recommendations, the application retrieves relevant information from a nutrition PDF through a local FAISS vector database and provides that context to the AI model before generating a response.

⚠️ Disclaimer: This project provides general health and nutrition information for educational and wellness purposes. It does not diagnose diseases, prescribe medicines, or replace professional medical advice.

✨ Features

Feature

Description

🧮 BMI Calculator

Calculates Body Mass Index from height and weight

🔥 BMR Calculator

Estimates Basal Metabolic Rate

⚡ TDEE Calculator

Estimates daily energy expenditure based on activity

🎯 Calorie Target

Calculates an estimated calorie target based on the selected goal

🥗 AI Diet Recommendation

Generates a one-day meal plan using retrieved nutrition knowledge

🔎 RAG Search

Retrieves relevant information from the nutrition knowledge base

💬 Health Assistance

Answers nutrition and health-related questions

🥦 Diet Preference

Supports vegetarian and non-vegetarian preferences

⚠️ Allergy Awareness

Includes user-provided allergy information in recommendations

🧠 How It Works

🔄 RAG Pipeline

                 ┌─────────────────────┐
                 │  Nutrition PDF      │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │   PDF Loader        │
                 │   PyPDFLoader       │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │  Text Splitting     │
                 │  Chunking           │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ HuggingFace         │
                 │ Embeddings          │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ FAISS Vector DB     │
                 └──────────┬──────────┘
                            ↓
              ┌─────────────┴─────────────┐
              ↓                           ↓
       User Diet Request           Health Question
              ↓                           ↓
              └─────────────┬─────────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Similarity Search   │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Relevant Context    │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │     AI Model        │
                 └──────────┬──────────┘
                            ↓
                 ┌─────────────────────┐
                 │ Final AI Response   │
                 └─────────────────────┘

📊 Health Calculation Flow

User Information
      ↓
Height + Weight
      ↓
     BMI
      ↓
Age + Gender + Height + Weight
      ↓
     BMR
      ↓
Activity Level
      ↓
     TDEE
      ↓
Fitness Goal
      ↓
Calorie Target

🖥️ Application Interface

The application contains two main sections:

🥗 Diet Recommendation

The user selects personal information and clicks Recommend Diet.

The system:

Collects user information.

Calculates BMI, BMR, TDEE, and calorie target.

Searches the nutrition vector database.

Retrieves relevant nutrition context.

Sends the context and user information to the AI model.

Generates a one-day diet recommendation.

💬 Health Assistance

The user enters a health or nutrition question.

Question
   ↓
FAISS Similarity Search
   ↓
Relevant Nutrition Context
   ↓
AI Model
   ↓
Answer

🛠️ Tech Stack

Programming

🐍 Python

Frontend / UI

Streamlit

AI / LLM

Hugging Face Router

OpenAI-compatible Python SDK

openai/gpt-oss-120b

RAG

LangChain

FAISS

HuggingFace Embeddings

Sentence Transformers

Document Processing

PyPDF

Configuration

python-dotenv

📁 Project Structure

AI-Health-Assistant/
│
├── app.py                  # Main Streamlit application
├── diet.py                 # BMI, BMR, TDEE and calorie calculations
├── rag.py                  # RAG creation and loading
├── create_database.py      # Creates the FAISS database
├── requirements.txt        # Project dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignored files
├── .env                    # API key - local only
│
├── data/
│   └── nutrition.pdf       # Nutrition knowledge source
│
└── vector_db/
    ├── index.faiss         # FAISS index
    └── index.pkl           # Stored document metadata

⚙️ Installation

1️⃣ Clone the Repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Health-Assistant

2️⃣ Create a Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3️⃣ Install Dependencies

pip install -r requirements.txt

If requirements.txt is not available:

pip install streamlit openai python-dotenv langchain-community langchain-text-splitters langchain-huggingface faiss-cpu pypdf sentence-transformers

🔐 Environment Setup

Create a file named:

.env

Add your Hugging Face token:

HF_TOKEN=your_hugging_face_token

The API key should never be hard-coded into app.py or uploaded to GitHub.

🗄️ Create the RAG Database

Make sure the nutrition PDF exists at:

data/nutrition.pdf

Then run:

python create_database.py

Expected output:

Creating database...
database created

This creates the local:

vector_db/

directory.

▶️ Run the Application

Start Streamlit:

python -m streamlit run app.py

Then open:

http://localhost:8501

📦 requirements.txt

streamlit
openai
python-dotenv
langchain-community
langchain-text-splitters
langchain-huggingface
faiss-cpu
pypdf
sentence-transformers

🔒 .gitignore

.env
__pycache__/
*.py[cod]
venv/
.venv/
vector_db/
.streamlit/secrets.toml
.vscode/
.idea/
*.log

🔐 Never commit .env because it contains your API credentials.

🚀 Future Improvements

🔐 User authentication

☁️ Cloud-based database

📅 Weekly and monthly meal plans

📈 Health progress tracking

📊 Nutrition charts

🍎 Larger food and nutrition database

📄 Downloadable diet plans

🌐 Multilingual support

📱 Mobile-friendly interface

🔔 Personalized reminders

🧠 Improved RAG evaluation

🛡️ Stronger validation and safety checks

🧪 Example Use Case

Input
├── Age: 20
├── Gender: Male
├── Weight: 70 kg
├── Height: 175 cm
├── Activity: Moderately Active
├── Goal: Weight Maintain
├── Diet: Vegetarian
└── Allergy: None

             ↓

BMI → BMR → TDEE → Calorie Target

             ↓

Nutrition Knowledge Retrieval

             ↓

AI Generation

             ↓

🥗 Personalized One-Day Diet Plan

⚠️ Health & Safety

This application is designed for educational and general wellness purposes.

It should not be used to:

Diagnose medical conditions

Prescribe medication

Replace professional medical consultation

Claim that a food or diet can cure a disease

For serious or persistent health concerns, consult a qualified healthcare professional.

👨‍💻 Author

Manav Chaudhary

CSE Student | Python Developer | AI & Generative AI Learner

Currently exploring:

Python • Full Stack Development • Generative AI • RAG • Streamlit

⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

<p align="center">
  Built with 🐍 Python + ⚡ Streamlit + 🧠 RAG + 🤖 Generative AI
</p>
