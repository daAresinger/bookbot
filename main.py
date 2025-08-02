from stats import count_words, count_chars, report
import sys

def get_book_text(path):
    with open(path) as f:
        print(f.read())


def main():
    if len(sys.argv)<2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    report(sys.argv[1])

main()
