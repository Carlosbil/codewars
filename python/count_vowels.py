#want to try a different way for make it, but still better just reade letters and count sum if its vowel like:
#sum(c in 'aeiou' for c in s)
def get_count(sentence):
    vowels = ["a","e","i","o","u"]
    total = 0
    for x in range(0,5) :
        x = vowels[x]
        total += sentence.count(x)
        print(total)
    return total