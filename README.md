<div align="center">

# 🧠 AI Health Assistant

### AI-Powered Health, Nutrition & Personalized Diet Recommendation System

<p>
  <a href="https://project-health-assistant-manav.streamlit.app/">
    <img src="https://img.shields.io/badge/🚀_LIVE_DEMO-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  </a>
  <a href="https://github.com/techwithmanav/project-health-Assistant">
    <img src="https://img.shields.io/badge/💻_SOURCE_CODE-GitHub-181717?style=for-the-badge&logo=github&logoColor=white" />
  </a>
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white" />
  <img src="https://img.shields.io/badge/FAISS-Vector_DB-00A67E?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-AI-8A2BE2?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Generative_AI-🤖-FF6F00?style=for-the-badge" />
</p>

<p>
  <strong>Calculate • Retrieve • Understand • Generate</strong>
</p>

<p>
  An intelligent wellness application that combines health calculations,
  nutrition knowledge retrieval, vector search, and Generative AI
  to provide personalized diet recommendations and nutrition assistance.
</p>

<br>

<a href="https://project-health-assistant-manav.streamlit.app/">
  <img src="https://img.shields.io/badge/▶_TRY_THE_LIVE_APPLICATION-NOW-00C853?style=for-the-badge&logo=streamlit&logoColor=white" />
</a>

</div>

---

## 🌟 Overview

**AI Health Assistant** is an AI-powered wellness and nutrition application built with **Python and Streamlit**.

The system combines traditional health calculations with a **Retrieval-Augmented Generation (RAG)** pipeline to provide contextual AI-generated nutrition assistance.

Users can enter basic information such as:

* 👤 Age
* ⚧️ Gender
* ⚖️ Weight
* 📏 Height
* 🏃 Activity Level
* 🎯 Fitness Goal
* 🥗 Diet Preference
* ⚠️ Food Allergies

The application then calculates:

**BMI → BMR → TDEE → Estimated Calorie Target**

For AI-powered recommendations, the application retrieves relevant information from a nutrition knowledge base using **FAISS vector search** and provides the retrieved context to the AI model before generating a response.

---

# 🚀 Live Application

<div align="center">

<a href="https://project-health-assistant-manav.streamlit.app/">
<img src="https://img.shields.io/badge/🚀_OPEN_AI_HEALTH_ASSISTANT-CLICK_HERE-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</a>

<br><br>

**Live Demo**

https://project-health-assistant-manav.streamlit.app/

</div>

---

# ✨ Key Features

<table>
<tr>
<td width="50%">

### 🧮 Health Calculations

* ⚖️ BMI Calculation
* 🔥 BMR Estimation
* ⚡ TDEE Calculation
* 🎯 Calorie Target Estimation

</td>

<td width="50%">

### 🤖 AI Assistance

* 💬 Health & Nutrition Q&A
* 🥗 AI Diet Recommendations
* 🧠 Generative AI
* 🔎 Context-Aware Responses

</td>
</tr>

<tr>
<td>

### 🧠 RAG Pipeline

* 📄 Nutrition PDF Knowledge Base
* ✂️ Document Chunking
* 🔤 Embeddings
* 🗄️ FAISS Vector Database
* 🔎 Similarity Search

</td>

<td>

### 🥗 Personalized Nutrition

* 👤 User Profile Inputs
* 🥦 Vegetarian / Non-Vegetarian
* ⚠️ Allergy Awareness
* 🍽️ One-Day Meal Plan
* 📊 Approximate Nutrition Information

</td>
</tr>
</table>

---

# 🧠 How the AI Works

The core intelligence of the project is built around **Retrieval-Augmented Generation (RAG)**.

Instead of relying only on the language model's internal knowledge, the application first searches a nutrition knowledge base and retrieves relevant information.

### 🔄 RAG Architecture

```mermaid
flowchart TD

    A[📄 Nutrition PDF] --> B[📑 PDF Loader]
    B --> C[✂️ Text Splitting]
    C --> D[🧠 HuggingFace Embeddings]
    D --> E[🗄️ FAISS Vector Database]

    U[👤 User Question / Diet Request] --> F[🔎 Similarity Search]
    E --> F

    F --> G[📚 Relevant Nutrition Context]
    G --> H[🤖 Generative AI Model]
    H --> I[💬 Personalized AI Response]

    style A fill:#E3F2FD
    style E fill:#FFF3E0
    style H fill:#F3E5F5
    style I fill:#E8F5E9
```

### 🔍 RAG Process

```text
Nutrition Knowledge
       │
       ▼
   PDF Loading
       │
       ▼
 Text Extraction
       │
       ▼
 Text Chunking
       │
       ▼
   Embeddings
       │
       ▼
 FAISS Vector DB
       │
       ▼
 User Question
       │
       ▼
Similarity Search
       │
       ▼
Relevant Context
       │
       ▼
  Generative AI
       │
       ▼
Personalized Answer
```

---

# 🏗️ System Architecture

```mermaid
flowchart LR

    USER[👤 User]

    UI[🖥️ Streamlit Interface]

    CALC[🧮 Health Calculator]
    RAG[🧠 RAG Engine]

    BMI[⚖️ BMI]
    BMR[🔥 BMR]
    TDEE[⚡ TDEE]
    CAL[🎯 Calorie Target]

    PDF[📄 Nutrition PDF]
    EMB[🔤 Embeddings]
    FAISS[(🗄️ FAISS)]

    SEARCH[🔎 Similarity Search]
    CONTEXT[📚 Retrieved Context]
    AI[🤖 Generative AI]
    RESPONSE[💬 AI Response]

    USER --> UI

    UI --> CALC
    UI --> RAG

    CALC --> BMI
    BMI --> BMR
    BMR --> TDEE
    TDEE --> CAL

    PDF --> EMB
    EMB --> FAISS

    RAG --> SEARCH
    FAISS --> SEARCH
    SEARCH --> CONTEXT
    CONTEXT --> AI

    CAL --> AI
    AI --> RESPONSE
    RESPONSE --> UI
```

---

# 🧮 Health Calculation Engine

The application performs a sequence of health-related calculations.

### Calculation Flow

```text
👤 User Information
        │
        ▼
📏 Height + ⚖️ Weight
        │
        ▼
⚖️ BMI
        │
        ▼
👤 Age + Gender + Height + Weight
        │
        ▼
🔥 BMR
        │
        ▼
🏃 Activity Level
        │
        ▼
⚡ TDEE
        │
        ▼
🎯 Fitness Goal
        │
        ▼
🍽️ Estimated Calorie Target
```

### Supported Calculations

| Calculation           | Purpose                        |
| --------------------- | ------------------------------ |
| ⚖️ **BMI**            | Body Mass Index                |
| 🔥 **BMR**            | Basal Metabolic Rate           |
| ⚡ **TDEE**            | Total Daily Energy Expenditure |
| 🎯 **Calorie Target** | Estimated daily calorie target |

---

# 🥗 Personalized Diet Recommendation

The application uses the user's provided information to generate a personalized one-day meal recommendation.

### Input

```text
👤 Gender
🎂 Age
⚖️ Weight
📏 Height
🏃 Activity Level
🎯 Health Goal
🥗 Diet Type
⚠️ Food Allergies
```

### Output

```text
🍳 Breakfast
        ↓
🥜 Morning Snack
        ↓
🍛 Lunch
        ↓
🍎 Evening Snack
        ↓
🍽️ Dinner
```

The generated recommendations can include:

* 🍽️ Food suggestions
* 📏 Portion information
* 🔥 Approximate calories
* 💪 Approximate protein
* ⚠️ Allergy-aware considerations

---

# 💬 Health & Nutrition Assistant

Users can also ask nutrition-related questions.

### Example Questions

```text
"What are good sources of vegetarian protein?"

"What are healthy breakfast options?"

"How can I increase my protein intake?"

"What foods are rich in nutrients?"

"What are some healthy sources of carbohydrates?"
```

### Response Pipeline

```text
💬 User Question
       ↓
🔎 FAISS Similarity Search
       ↓
📚 Relevant Nutrition Context
       ↓
🤖 Generative AI
       ↓
💡 Context-Aware Answer
```

---

# 🛠️ Technology Stack

<div align="center">

| Layer               | Technology                                         |
| ------------------- | -------------------------------------------------- |
| 🐍 Programming      | **Python**                                         |
| 🖥️ Web Interface   | **Streamlit**                                      |
| 🤖 AI / LLM         | **Hugging Face Router + OpenAI-compatible SDK**    |
| 🧠 Model            | **openai/gpt-oss-120b**                            |
| 🔎 RAG              | **LangChain**                                      |
| 🗄️ Vector Database | **FAISS**                                          |
| 🔤 Embeddings       | **HuggingFace Embeddings / Sentence Transformers** |
| 📄 PDF Processing   | **PyPDF**                                          |
| 🔐 Configuration    | **python-dotenv**                                  |
| ☁️ Deployment       | **Streamlit Community Cloud**                      |

</div>

---

# 📂 Project Structure

```text
project-health-Assistant/
│
├── 📄 app.py
│   └── Main Streamlit application
│
├── 📄 diet.py
│   └── BMI, BMR, TDEE & calorie calculations
│
├── 📄 rag.py
│   └── RAG creation and retrieval logic
│
├── 📄 create_database.py
│   └── FAISS vector database creation
│
├── 📄 llm_test.py
│   └── LLM testing
│
├── 📄 requirements.txt
│   └── Python dependencies
│
├── 📄 LICENSE
│
├── 📁 data/
│   └── 📄 nutrition.pdf
│
└── 📄 README.md
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/techwithmanav/project-health-Assistant.git
cd project-health-Assistant
```

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```env
HF_TOKEN=your_hugging_face_token
```

⚠️ **Never upload your `.env` file or API credentials to GitHub.**

---

# 🗄️ Build the Vector Database

Make sure the nutrition knowledge file exists:

```text
data/nutrition.pdf
```

Then run:

```bash
python create_database.py
```

This creates the local FAISS vector database used by the RAG pipeline.

---

# ▶️ Run Locally

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

Open:

```text
http://localhost:8501
```

---

# ☁️ Deployment

The application is deployed using **Streamlit Community Cloud**.

### Deployment Flow

```text
💻 GitHub Repository
        │
        ▼
☁️ Streamlit Community Cloud
        │
        ▼
📦 Install Dependencies
        │
        ▼
🔐 Configure Secrets
        │
        ▼
🚀 Deploy Application
        │
        ▼
🌐 Live Web Application
```

### Live Deployment

🚀 **https://project-health-assistant-manav.streamlit.app/**

---

# 🔐 Security

API credentials should never be hard-coded into the application.

### ❌ Avoid

```python
HF_TOKEN = "my-secret-token"
```

### ✅ Use environment variables / Streamlit secrets

```python
st.secrets["HF_TOKEN"]
```

or:

```python
from dotenv import load_dotenv
import os

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
```

Recommended `.gitignore` entries:

```text
.env
venv/
.venv/
__pycache__/
*.py[cod]
.streamlit/secrets.toml
*.log
```

---

# 📊 Application Workflow

```mermaid
flowchart TD

    A[👤 Enter Personal Information] --> B[⚖️ Calculate BMI]
    B --> C[🔥 Calculate BMR]
    C --> D[⚡ Calculate TDEE]
    D --> E[🎯 Calculate Calorie Target]

    E --> F{What does the user need?}

    F -->|🥗 Diet Plan| G[🔎 Retrieve Nutrition Context]
    F -->|💬 Health Question| G

    G --> H[🗄️ FAISS Similarity Search]
    H --> I[📚 Relevant Context]
    I --> J[🤖 Generative AI]
    J --> K[💡 Personalized Response]

    style A fill:#E3F2FD
    style J fill:#F3E5F5
    style K fill:#E8F5E9
```

---

# 🎯 Project Objectives

This project demonstrates practical implementation of:

* 🐍 Python application development
* 🖥️ Streamlit web applications
* 🧮 Mathematical health calculations
* 🤖 Generative AI integration
* 🧠 Retrieval-Augmented Generation
* 🔎 Semantic similarity search
* 🗄️ Vector databases
* 🔤 Text embeddings
* 📄 PDF knowledge retrieval
* 🔐 Environment-based secret management
* ☁️ Cloud deployment

---

# 💡 What Makes This Project Interesting?

The project combines multiple modern AI application concepts into one working application:

```text
              ┌──────────────────────┐
              │      Streamlit       │
              │      Web App         │
              └──────────┬───────────┘
                         │
              ┌──────────▼───────────┐
              │  Health Calculations │
              │ BMI • BMR • TDEE     │
              └──────────┬───────────┘
                         │
              ┌──────────▼───────────┐
              │        RAG            │
              │ Retrieval + Context  │
              └──────────┬───────────┘
                         │
              ┌──────────▼───────────┐
              │       FAISS           │
              │    Vector Search      │
              └──────────┬───────────┘
                         │
              ┌──────────▼───────────┐
              │    Generative AI      │
              │   Context-Aware LLM   │
              └──────────┬───────────┘
                         │
              ┌──────────▼───────────┐
              │ Personalized Output  │
              └──────────────────────┘
```

---

# 🔮 Future Improvements

Potential future enhancements include:

* 🔐 User authentication
* ☁️ Cloud-based persistent database
* 📅 Weekly meal planning
* 📆 Monthly meal planning
* 📈 Health progress tracking
* ⚖️ Weight tracking
* 📊 Nutrition visualization
* 🛒 Grocery list generation
* 📄 Downloadable diet plans
* 🌐 Multilingual support
* 📱 Improved mobile experience
* 🔔 Personalized reminders
* 🧠 Improved RAG evaluation
* 🛡️ Additional validation and safety checks

---

# ⚠️ Health & Safety Disclaimer

> **This application is intended for educational and general wellness purposes only.**

The information generated by this application should **not** be considered a substitute for professional medical advice, diagnosis, or treatment.

This application should not be used to:

* Diagnose medical conditions
* Prescribe medication
* Replace professional medical consultation
* Claim that a particular food or diet can cure a disease

For serious or persistent health concerns, consult a qualified healthcare professional.

---

# 👨‍💻 Developer

<div align="center">

## Manav Chaudhary

**CSE Student | Python Developer | AI & Generative AI Learner**

### Currently Exploring

🐍 Python
⚡ Full Stack Development
🤖 Generative AI
🧠 Retrieval-Augmented Generation
🖥️ Streamlit

<br>

<a href="https://github.com/techwithmanav">
<img src="https://img.shields.io/badge/GitHub-techwithmanav-181717?style=for-the-badge&logo=github&logoColor=white" />
</a>

</div>

---

# 📈 GitHub Profile

<div align="center">

<img src="https://github-readme-stats.vercel.app/api?username=techwithmanav&show_icons=true&theme=tokyonight&hide_border=true" />

<br><br>

<img src="https://github-readme-stats.vercel.app/api/top-langs/?username=techwithmanav&layout=compact&theme=tokyonight&hide_border=true" />

<br><br>

<img src="https://streak-stats.demolab.com?user=techwithmanav&theme=tokyonight&hide_border=true" />

</div>
----

<div align="center">

### 🧠 AI Health Assistant

**Built with Python • Streamlit • RAG • FAISS • Generative AI**

<br>

🚀 **Live Demo:**
https://project-health-assistant-manav.streamlit.app/

<br>

💻 **Source Code:**
https://github.com/techwithmanav/project-health-Assistant

<br><br>

**Made with ❤️ by Manav Chaudhary**

</div>
