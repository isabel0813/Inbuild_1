from fastapi import FastAPI
from pydantic import BaseModel
import sqlite3
from text_utils import clean_text, split_words, count_words, top_n_words

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def init_db():
    conn = sqlite3.connect("analysis.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS analysis_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_text TEXT,
        top_word TEXT,
        top_count INTEGER
    )
    """)
    conn.commit()
    conn.close()

init_db()

class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze(input: TextInput):
    cleaned = clean_text(input.text)
    words = split_words(cleaned)
    counts = count_words(words)
    top_words = top_n_words(counts, n=1)
    word, count = top_words[0]

    conn = sqlite3.connect("analysis.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO analysis_log (input_text, top_word, top_count) VALUES (?, ?, ?)",
        (input.text, word, count)
    )
    conn.commit()
    conn.close()

    return {"input_text": input.text, "top_word": word, "top_count": count}

@app.get("/results")
def get_results():
    conn = sqlite3.connect("analysis.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM analysis_log")
    rows = cursor.fetchall()
    conn.close()
    return {"results": rows}