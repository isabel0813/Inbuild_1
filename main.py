from text_utils import clean_text, split_words, count_words, top_n_words

text = input("확인할 문장을 입력하세요: ")

cleaned = clean_text(text)
words = split_words(cleaned)
counts = count_words(words)
top_words = top_n_words(counts, n=1)
word, count = top_words[0]

print("\n입력한 문장:", text)
print("단어별 등장 횟수:", counts)
print(f"가장 많이 나온 단어: '{word}' ({count}번)")