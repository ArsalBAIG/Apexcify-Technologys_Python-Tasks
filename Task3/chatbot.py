qna = {
    'hi': 'hi there!',
    'how are you': 'great whats about you?',
    'what is your name': 'my name is Arsal.',
    'what is your age?': 'my age is 20.'
}

while True:
    qs = input("Ask a question (or type 'quit' to exit): ").lower()
    if qs == 'quit':
        break
    elif qs in qna:
        print(qna[qs])
    else:
        print("I don't have an answer for that question.")