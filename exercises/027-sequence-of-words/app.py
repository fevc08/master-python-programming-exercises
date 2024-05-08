def sequence_of_words(words):
    words_splited = []
    for word in words.split(","):
        words_splited.append(word)

    return print(", ".join(sorted(words_splited, key=)))


sequence_of_words("without,hello,bag,world")
