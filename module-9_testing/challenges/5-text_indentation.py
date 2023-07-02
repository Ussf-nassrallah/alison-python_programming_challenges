
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    n = len(text)
    char = 0

    while char < n and text[char] == '':
        char += 1

    while char < n:
        print(text[char], end="")
        if text[char] == '\n' or text[char] in '.?:':
            if text[char] in '.?:':
                print('\n')
            char += 1

            while char < n and text[char] == ' ':
                char += 1
            continue
        char += 1