from random import choice
from string import ascii_lowercase


class Hangman:
    def __init__(self):
        self.attempts = 8
        self.possible_words = 'python', 'java', 'swift', 'javascript'
        self.cur_word = None
        self.inputted = None
        self.guessed = None
        self.win_times = 0
        self.lose_times = 0

    def get_guessed_word(self):
        word = map(lambda a: a if a in self.guessed else '-', self.cur_word)
        return ''.join(word)

    def input_letter(self):
        letter = input('Input a letter: ')
        if len(letter) != 1:
            print('Please, input a single letter.')
            return None
        elif letter not in ascii_lowercase:
            print('Please, enter a lowercase letter',
                  'from the English alphabet.')
            return None
        elif letter in self.inputted:
            print("You've already guessed this letter.")
        elif letter not in self.cur_word:
            self.attempts -= 1
            print(f"That letter doesn't appear in the word. ",
                  f" # {self.attempts} attempts")

        self.inputted.add(letter)

        return letter

    def guess_word(self):
        while self.attempts > 0:
            guessed_word = self.get_guessed_word()

            if self.cur_word == guessed_word:
                print(f'You guessed the word {guessed_word}!')
                print('You survived!')
                self.win_times += 1
                break

            print(f'{guessed_word}\n')

            letter = self.input_letter()
            if letter:
                self.guessed.add(letter)
        else:
            print('\nYou lost!')
            self.lose_times += 1

    def play(self):
        self.cur_word = choice(self.possible_words)
        self.inputted = set()
        self.guessed = set()
        self.guess_word()
        self.prompt_action()

    def results(self):
        print(f'You won: {self.win_times} times.')
        print(f'You lost: {self.lose_times} times.')
        self.prompt_action()

    def prompt_action(self):
        action = input(' '.join([
            'Type "play" to play the game,',
            '"results" to show the scoreboard, and "exit" to quit: '
        ]))

        if action not in ('play', 'results', 'exit'):
            return self.prompt_action()
        elif action != 'exit':
            return getattr(self, action)()

    def start(self):
        print(f'H A N G M A N # {self.attempts} attempts')
        self.prompt_action()


def main():
    Hangman().start()


if __name__ == '__main__':
    main()
