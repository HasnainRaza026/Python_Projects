import string

alphabets = string.ascii_lowercase
shift = 3


def encode(msg):
    global shift
    shift = int(input("Enter shift: "))
    return ''.join(alphabets[(alphabets.index(c) + shift) % 26] if c in alphabets else c for c in msg)


def decode(msg, shift):
    return ''.join(alphabets[(alphabets.index(c) - shift) % 26] if c in alphabets else c for c in msg)


def main():
    mode = input(
        "Type 'encode' to encode a message, type 'decode' to decode a message: ").lower()
    msg = input("Enter a message, without spaces between: ").lower()

    if mode == "encode":
        enc_msg = encode(msg)
        print("Encoded message:", enc_msg)
    elif mode == "decode":
        dec_msg = decode(msg, shift)
        print("Decoded message:", dec_msg)

    cn = input("type 'yes' to continue, and 'no' end: ").lower()
    if cn == "yes":
        main()
    elif cn == "no":
        pass


if __name__ == "__main__":
    main()
