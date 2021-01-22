# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self._word = word
        self._masked_word = list(len(word) * "_")

    def guess(self, char):
        if self.status != STATUS_ONGOING:
            raise ValueError("GAME OVER")

        if self._word.find(char) == -1 or self._masked_word.count(char) != 0:
            self.remaining_guesses -= 1
            if self.remaining_guesses == -1:
                self.status = STATUS_LOSE
        else:
            index_letter_found = self._word.find(char,0)        
            while index_letter_found != -1 and index_letter_found < len(self._word) + 1:
                self._masked_word[index_letter_found] = char                
                index_letter_found = self._word.find(char,index_letter_found + 1)   
        
            if "".join(self._masked_word) == self._word:
                self.status = STATUS_WIN
                return "You WIN"
            else:
                return False

    def get_masked_word(self):
        return "".join(self._masked_word)

    def get_status(self):
        return self.status


if __name__ == "__main__":
    game = Hangman("hello")
    
    print (game.get_masked_word())
    game.guess("h")
    game.guess("e")
    game.guess("l")
    print (game.get_masked_word())
    game.guess("l")
    game.guess("o")    
    print(game.get_status())
    print (game.get_masked_word())

    
    print(F"remaining guesses {game.remaining_guesses}")