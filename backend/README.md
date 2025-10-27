#  AI Wiki Quiz Generator – Backend

## Overview
This backend powers the **AI Wiki Quiz Generator**, a system that automatically generates quizzes from any Wikipedia article using Large Language Models (LLMs).  
It handles Wikipedia scraping, quiz creation, and database storage.

## Tech Stack
- **Python 3.10+**
- **FastAPI**
- **SQLite / SQLAlchemy**
- **Requests / BeautifulSoup4**
- **OpenAI / HuggingFace API**

## Folder Structure
backend/
├── main.py
├── core_logic.py
├── database.py
├── db_models.py
├── requirements.txt
└── README.md
##  Setup Instructions
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
Author

Built by Ayesha Mohammad
