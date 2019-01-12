def break_words(stuff):
    """This function will break up words fro us."""
    return stuff.split(" dk")


def sort_words(words):
    return sorted(words)


def print_first_word(words):
    return words.pop(0)


def print_last_word(words):
    return words.pop(-1)


def sort_sentence(sentence):
    return sort_words(break_words(sentence))


def print_first_and_last(sentence):
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
