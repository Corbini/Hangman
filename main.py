import random

words_list = []


def load_from_file(words_file):
    with open(words_file, 'r') as file:
        for line in file:
            words_list.append(line)


def check_letters(word):
    for letter in word:
        if word == "!q":
            return True
        if letter.isupper():
            print("Don't use Upper letters")
            return False
        if letter.isalpha():
            return True
        else:
            print("Don't use symbols")
            return False


def player_input():
    while True:
        print("Enter word or letter: ", end="")
        player_input = input()
        if check_letters(player_input):
            return player_input


def check_for_words(question, word):
    return True


def check_for_letters(letter, word):
    return True


def check(question, word):
    if len(question) > 1:
        return check_for_words(question, word)
    else:
        return check_for_letters(question, word)


def main():

    load_from_file("words.txt")

    print("Game starts")
    print("Write !q do quit")
    print("Write letter or word to guess")

    random_int = random.randint(0, len(words_list))
    word_to_guess = words_list[random_int]
    print("word to guess: ", word_to_guess)

    while True:
        question = player_input()
        print(question)

        if question == "!q":
            print("Bye")
            return

        if check(question, word_to_guess):
            # you win, next round
            pass


random.seed()
main()
