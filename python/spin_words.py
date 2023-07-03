def spin_words(sentence):
    #take all the words of the sentence
    words = sentence.split()
    for i in range(len(words)):
        #if length is 5 or greater, then reverse
        if len(words[i]) >= 5:
            #reverse the word
            words[i] = words[i][::-1]
    return ' '.join(words)