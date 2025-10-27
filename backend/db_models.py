from sqlalchemy import Column, Integer, String, JSON
from database import Base

class Quizzes(Base):
    __tablename__ = "quizzes"
    id = Column(Integer, primary_key=True, index=True)
    url = Column(String)
    quiz_data = Column(JSON)
