import sys

from hittagenus import get_genus, print_genus


def main():
    words = set(sys.argv[1:])

    for word in words:
        genus_info = get_genus(word)
        print_genus(word, genus_info)


if __name__ == "__main__":
    main()
