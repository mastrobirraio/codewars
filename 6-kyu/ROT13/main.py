def rot13_decode(message):
    key = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    val = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
    translator = dict(zip(key, val))
    return ''.join([translator.get(c, c) for c in message])


def main():
    print(rot13_decode('EBG13 rknzcyr'))
    print(rot13_decode('This is my first ROT13 excercise!'))


if __name__ == '__main__':
    main()
