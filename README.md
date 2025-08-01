# 🧠 Portfolio Website Generator Backend (Flask API)

This project provides a backend Flask API that allows users to:
- Upload resumes (PDF/DOC) and extract structured information
- Translate website content into multiple languages
- Display pricing in multiple currencies based on location
- Use an AI-powered Facebook Growth Agent to auto-generate content

---

## 📦 Features

### 1. Resume Upload & Portfolio JSON Generation
- Upload `.pdf` or `.docx` resumes
- Extract Name, Bio, Skills, Education, Experience
- Return structured JSON data to populate portfolio websites

### 2. Multi-Lingual Content Translation
- Translate site content using `/translate`
- Accepts language codes like `hi`, `fr`, `es`, etc.

### 3. Multi-Currency Pricing Display
- Endpoint returns product pricing in user’s local currency
- Based on query param: `?country=IN`, `?country=US`, etc.

### 4. AI Facebook Growth Agent (Mocked)
- Input: business website URL + optional industry
- Generates content ideas:
  - Business tips
  - Promotional offers
  - Industry insights
- Content planner with post frequency, tone, and type mix
- Preview, edit, and simulate auto-posting to Facebook

---

## 🚀 Getting Started

### 1. Clone Repo
```bash
 git clone https://github.com/yourusername/portfolio-backend.git
 cd portfolio-backend
 ```

### 2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run the Server
python main.py

### Flask will start at http://127.0.0.1:5000/