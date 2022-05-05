import random


words_list = []
player_progress = ""


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
    if question == word:
        global player_progress
        player_progress = word
        return True
    return False


def check_for_letters(letter, word):
    if letter in word:
        # player_progress[word.] = letter
        pass
    if player_progress == word:
        return True
    return False


def check(question, word):
    if len(question) > 1:
        return check_for_words(question, word)
    else:
        return check_for_letters(question, word)


def random_word():
    random_int = random.randint(0, len(words_list))
    word_to_guess = words_list[random_int][:-1]
    print("word to guess: ", word_to_guess)

    global player_progress
    player_progress = "_" * len(word_to_guess)

    return word_to_guess


def main():

    load_from_file("words.txt")

    print("Game starts")
    print("Write !q do quit")
    print("Write letter or word to guess")

    word_to_guess = random_word()
    global player_progress

    while True:
        print(player_progress)

        question = player_input()
        print(question)

        if question == "!q":
            print("Bye")
            return

        if check(question, word_to_guess):
            print("you win")
            word_to_guess = random_word()

            pass


random.seed()
main()
