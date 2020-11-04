# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.word = word
        self.masked = ''.join(['_' for char in self.word])
        self.guessed_chars = []

    def guess(self, char):
        if self.status == STATUS_WIN:
            raise ValueError('the game is over')
        if self.remaining_guesses < 0:
            self.status == STATUS_LOSE
            raise ValueError('the game is over')
        
        if char not in self.guessed_chars:
            self.guessed_chars.append(char)
            if char in self.word:
                for index, letter in enumerate(self.word):
                    if char == letter:
                        split = [_ for _ in self.masked] 
                        split[index] = char 
                        self.masked = ''.join(split)
            else:
               self.remaining_guesses -= 1 
        else:
            self.remaining_guesses -= 1


    def get_masked_word(self):
        return self.masked 
    

    def get_status(self):
        if self.get_masked_word() == self.word:
            self.status = STATUS_WIN
        elif self.remaining_guesses < 0:
            self.status = STATUS_LOSE
        return self.status
          


