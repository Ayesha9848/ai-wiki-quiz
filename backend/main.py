from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from models import URLInput, QuizOutput
from db_models import Quizzes
from database import get_db, init_db
from core_logic import scrape_wikipedia_article, generate_quiz_with_llm

app = FastAPI(title="AI Wiki Quiz Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.post("/api/v1/generate-quiz", response_model=QuizOutput)
def generate_quiz(input_data: URLInput, db: Session = Depends(get_db)):
    url = input_data.url
    existing = db.query(Quizzes).filter(Quizzes.url == url).first()
    if existing:
        return QuizOutput.from_orm(existing)

    scraped = scrape_wikipedia_article(url)
    quiz = generate_quiz_with_llm(scraped["article_text"], scraped["sections"])

    new_quiz = Quizzes(
        url=url,
        title=scraped["title"],
        summary=quiz.summary,
        key_entities=quiz.key_entities,
        sections=quiz.sections,
        quiz_data=quiz.quiz,
        related_topics=quiz.related_topics,
        raw_html=scraped["raw_html"]
    )
    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)
    return QuizOutput.from_orm(new_quiz)

@app.get("/api/v1/quizzes")
def get_all(db: Session = Depends(get_db)):
    return db.query(Quizzes.id, Quizzes.url, Quizzes.title, Quizzes.created_at).all()

@app.get("/api/v1/quizzes/{quiz_id}", response_model=QuizOutput)
def get_one(quiz_id: int, db: Session = Depends(get_db)):
    quiz = db.query(Quizzes).filter(Quizzes.id == quiz_id).first()
    if not quiz:
        raise HTTPException(404, "Quiz not found")
    return QuizOutput.from_orm(quiz)
