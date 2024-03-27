# abcdefghijklmnopqrstuvwxyz
def rot13(text):
    text = text.lower()
    alphabet = (
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
        'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
        's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    mapped = {lit: alphabet[(idx + 13) % 26] for idx, lit in enumerate(alphabet)}
    ciphered = ''
    for c in text:
        if c in alphabet:
            ciphered += mapped[c]
        else:
            ciphered += c
    return ciphered


def main():
    n = input("Choose option (1 - Encode, 2 - Decode): ")
    if n == '1':
        res = input("Enter text to encode: ")
        print("Encoded: ", rot13(res))
    elif n == '2':
        res = input("Enter text to decode: ")
        print("Decoded: ", rot13(res))
    else:
        print("Invalid option: \"", n, "\"!")


if __name__ == "__main__":
    main()
