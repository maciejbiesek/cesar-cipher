import argparse

alph = "abcdefghijklmnopqrstuvwxyz"
alph_upper = alph.upper()
alph_len = len(alph)

def prepare_data(file_path):
    with open(file_path, mode="r", encoding="utf-8") as f:
        text = ""
        for line in f:
            text += line

    return text

def encrypt(text, key):
    encrypted = ""
    for char in text:
        if char.isalpha():
            current_alph = alph if char.islower() else alph_upper
            try:
                char = current_alph[(current_alph.index(char) + key)%alph_len]
            except ValueError:
                pass
        encrypted += char

    return encrypted

def decrypt(text, key):
    decrypted = ""
    for char in text:
        if char.isalpha():
            current_alph = alph if char.islower() else alph_upper
            try:
                char = current_alph[(current_alph.index(char) - key)%alph_len]
            except ValueError:
                pass
        decrypted += char

    return decrypted

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str)
    parser.add_argument("key", type=int, nargs="?", default=3)
    parser.add_argument("--enc", dest='action', action='store_const',
                        const=encrypt)
    parser.add_argument("--dec", dest='action', action='store_const',
                        const=decrypt)
    args = parser.parse_args()

    if args.action is None:
        parser.parse_args(["-h"])
    try:
        text = prepare_data(args.filename)
        print(args.action(text, args.key))
    except FileNotFoundError:
        print("There's no file " + args.filename)
