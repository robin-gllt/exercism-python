


def is_isogram(string):

    allowed_char = [' ', '-', '_']

    string = string.lower()
    
    for letter in string:
        counter = string.count(letter)
       
        if letter not in allowed_char and counter > 1:            
            return False

    return True





#testing main
if __name__ == "__main__":
    is_isogram("thumbscrew-japingly")