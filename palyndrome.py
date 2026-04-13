def palyndrome(word):
    return word [::-1] == word

def palyndrome_recursive(word):
    if len(word)<=1:
        return True
    else:
        return (word[0] == word[-1] and palyndrome_recursive(word[1:-1]))

if __name__ == "__main__":
    print(palyndrome_recursive("casa"))
    print(palyndrome_recursive("civic"))