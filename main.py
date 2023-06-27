from random import randint
import string


def generator_password():
    n = randint(10, 15)
    symbols = string.hexdigits
    password = ""
    for i in range(n):
        password += symbols[randint(0, 21)]
    return password


def main():
    print(generator_password())


if __name__ == "__main__":
    main()
