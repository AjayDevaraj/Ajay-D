def main():
    y = input("Enter a character: ")

    if y in ('a', 'e', 'i', 'o', 'u'):
        print(y, "is a Vowel")
    else:
        print(y, "is a Consonant")

if __name__ == '__main__':
    main()
