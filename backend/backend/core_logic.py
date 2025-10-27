import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel
import random

class QuizData(BaseModel):
    summary: str
    key_entities: dict
    sections: list
    quiz: list
    related_topics: list

def scrape_wikipedia_article(url: str):
    response = requests.get(url)
    if response.status_code != 200:
        raise ValueError("Failed to fetch Wikipedia page.")
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.find("h1").text
    paragraphs = " ".join([p.text for p in soup.select("p")])
    sections = [h2.text for h2 in soup.select("h2")]
    return {"title": title, "article_text": paragraphs, "sections": sections, "raw_html": response.text}

def generate_quiz_with_llm(article_text: str, sections: list):
    # Simulated quiz generation (you can replace with Gemini API / LangChain)
    quiz = []
    for i in range(5):
        quiz.append({
            "question": f"Question {i+1} about {sections[i % len(sections)] if sections else 'topic'}?",
            "options": ["A", "B", "C", "D"],
            "answer": random.choice(["A", "B", "C", "D"]),
            "difficulty": random.choice(["easy", "medium", "hard"]),
            "explanation": "Generated explanation."
        })
    return QuizData(
        summary="Auto-generated summary of the article.",
        key_entities={"people": [], "organizations": [], "locations": []},
        sections=sections,
        quiz=quiz,
        related_topics=["Topic A", "Topic B"]
    )
