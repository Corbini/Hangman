import random
from enum import Enum

words_list = []
player_progress = ""
health = 0
used_guesses = []


class Checks (Enum):
    none_actions = 0
    win = 1
    minus_health = 2


def load_from_file(words_file):
    with open(words_file, 'r') as file:
        for line in file:
            words_list.append(line)


def check_letters(word):
    if word == "!q":
        return True

    if word == "":
        return False

    if word.isupper():
        print("Don't use Upper letters")
        return False

    if not word.isalpha():
        print("Don't use symbols")
        return False

    if word in words_list:
        print("You wrote it earlier")
        return False

    words_list.append(word)
    return True


def player_input():
    while True:
        print("Enter word or letter: ", end="")
        player_input = input()
        if check_letters(player_input):
            return player_input


def check_for_words(question, word):
    if question == word:
        global player_progress
        player_progress = word
        return Checks.win
    return Checks.minus_health


def check_for_letters(letter, word):
    global player_progress

    temp_progress = Checks.minus_health
    i = 0
    for w in word:
        if letter == w:
            player_progress = player_progress[:i] + letter + player_progress[i+1:]
            print("got a letter")
            temp_progress = Checks.none_actions
        i += 1

    if player_progress == word:
        temp_progress = Checks.win
    return temp_progress


def check(question, word):
    if len(question) > 1:
        return check_for_words(question, word)
    else:
        return check_for_letters(question, word)


def random_word():
    random_int = random.randint(0, len(words_list))
    word_to_guess = words_list[random_int][:-1]

    global player_progress
    player_progress = "_" * len(word_to_guess)

    global health
    health = 8

    global used_guesses
    del used_guesses
    used_guesses = []

    return word_to_guess


def main():

    load_from_file("words.txt")

    print("Game starts")
    print("Write !q do quit")
    print("Write letter or word to guess")

    word_to_guess = random_word()
    global player_progress
    global health

    while True:
        print(player_progress)

        question = player_input()

        if question == "!q":
            print("Bye")
            return

        check_status = check(question, word_to_guess)

        if check_status == Checks.win:
            print("you win")
            word_to_guess = random_word()
            continue

        if check_status == Checks.minus_health:
            health -= 1
            if health == 0:
                print("you lost")
                word_to_guess = random_word()
            else:
                print("you lost a health. Remaining: ", health)
            continue


random.seed()
main()
