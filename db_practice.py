import sqlite3
from text_utils import clean_text, split_words, count_words, top_n_words

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

text = input("확인할 문장을 입력하세요: ")
cleaned = clean_text(text)
words = split_words(cleaned)
counts = count_words(words)
top_words = top_n_words(counts, n=1)
word, count = top_words[0]

cursor.execute(
    "INSERT INTO analysis_log (input_text, top_word, top_count) VALUES (?, ?, ?)",
    (text, word, count)
)
conn.commit()

cursor.execute("SELECT * FROM analysis_log")
rows = cursor.fetchall()

print("\n저장된 기록들:")
for row in rows:
    print(row)

conn.close()