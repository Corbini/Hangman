

def load_from_file(words_file):
    pass


def player_input():
    # get 1 word or 1 letter or !q to quit
    pass


def check_for_words(question, word):
    return True


def check_for_letters(question, word):
    return True


def check(question, word):
    if len(question) > 1:
        return check_for_words(question, word)
    else:
        return check_for_letters(question, word)


def main():

    load_from_file("words.txt")

    print("Game starts")
    word_to_guess = ""  # pick random word from list

    while True:
        question = "test"
        # question = player_input()
        if question == "q!":
            break

        if check(question, word_to_guess):
            # you win, next round
            break


main()
