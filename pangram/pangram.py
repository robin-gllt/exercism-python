def is_pangram(sentence):
    
    for letter in range (97,123):
        if sentence.lower().find(chr(letter)) == -1:
            return False
            
    return True

if __name__ == '__main__':
    print(is_pangram("Five quacking Zephyrs jolt my wax bed"))
