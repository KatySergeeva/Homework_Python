import pytest
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Database setup
DATABASE_URL = "postgresql://postgres:123@localhost:5432/QA"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()


# Subject model
class Subject(Base):
    __tablename__ = 'subject'

    subject_id = Column(Integer, primary_key=True)
    subject_title = Column(String)


# Test for adding a subject
def test_add_subject():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()

    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Mathematics"

    session.delete(saved)
    session.commit()
    session.close()


def test_update_subject():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()
    subject.subject_title = "Latine"
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved.subject_title == "Latine"

    session.delete(saved)
    session.commit()
    session.close()


def test_delete_subject():
    session = Session()
    subject = Subject(subject_id=100, subject_title="Mathematics")
    session.add(subject)
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    session.delete(saved)
    session.commit()
    saved = session.query(Subject).filter_by(subject_id=100).first()
    assert saved is None

    session.close()