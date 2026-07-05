def clean_text(text):
    return text.lower().strip()

def split_words(text):
    return text.split()

def count_words(word_list):
    counter = {}
    for word in word_list:
        counter[word] = counter.get(word, 0) + 1
    return counter

def top_n_words(counter, n=5):
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)[:n]