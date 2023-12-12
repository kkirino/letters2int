import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="convert alphabetical column names to numbers"
    )
    parser.add_argument(
        "colname", type=str, help="alphabetical letters to convert into numbers"
    )
    args = parser.parse_args()

    def is_alphabet(letter):
       return  0 < (ord(letter.lower()) -96) < 27

    is_all_alphabets = all([is_alphabet(letter) for letter in args.colname])
    if is_all_alphabets:
        print(
            sum(
                [
                    (26 ** (len(args.colname) - index - 1)) * (ord(letter.lower()) - 96)
                    for index, letter in enumerate(args.colname)
                ]
            )
        )
        sys.exit(0)
    else:
        print(
            "InputError: column name should be alphabetical letters.", file=sys.stderr
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
