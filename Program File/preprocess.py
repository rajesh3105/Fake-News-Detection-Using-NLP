def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuations
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize the text
    words = word_tokenize(text)
    # Remove stopwords and words with length <= 2
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and len(word) > 2]
    # Remove repeated words
    words = list(dict.fromkeys(words))
    # Join the words back into text
    text = ' '.join(words)
    return text