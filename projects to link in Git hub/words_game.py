import random

def get_input():
    while True:
        user_input = input('Enter your guess: ')
        if user_input.isalpha():
            return user_input
        print('your input was not correct.try again.')

def get_input_from_list(words):
    user_input = get_input()

    while user_input.lower() not in words:
        print('You should guess word from the list.')
        print('please enter correct word!')
        user_input = get_input()



def print_game_intro():
    print('-' * 20)
    print('Hi welcome to the guess game.')
    print('All words here:', list_of_words)
    print('please start guessing!')
    print('-' * 20)

def run_game(number_of_rounds,words):
    print_game_intro()
    print(f'number of guesses: {number_of_rounds}')
    correct_word = random.choice(words)

    for i in range(number_of_rounds):
        user_input = get_input_from_list(words)

        if user_input == correct_word:
            print('YOU WON!')
            return
        else:
            print('You guessed wrong!')
            print(f'please try again! number of rounds left:{number_of_rounds - 1 - i}')
    print('You lost the game')


list_of_words = ['sun', 'flower', 'son', 'hello', 'hi', 'yesterday', 'tomorrow', 'moon', 'ola', 'paper']

run_game(5, list_of_words)