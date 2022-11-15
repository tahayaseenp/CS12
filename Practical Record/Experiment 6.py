def count_vowels():
    f = open("data.txt", "r")
    vowels = 0
    for line in f.readlines():
        for char in line:
            if char.lower() in 'aeiou':
                vowels += 1
    f.close()
    print("The number of vowels in the file is", vowels)


def count_consonants():
    f = open("data.txt", "r")
    consonants = 0
    for line in f.readlines():
        for char in line:
            if char.isalpha() and char.lower() not in 'aeiou':
                consonants += 1
    f.close()
    print("The number of consonants in the file is", consonants)


def count_lowercase():
    f = open("data.txt", "r")
    lowercase = 0
    for line in f.readlines():
        for char in line:
            if char.islower():
                lowercase += 1
    f.close()
    print("The number of lowercase letters in the file is", lowercase)


def count_uppercase():
    f = open("data.txt", "r")
    uppercase = 0
    for line in f.readlines():
        for char in line:
            if char.isupper():
                uppercase += 1
    f.close()
    print("The number of uppercase letters in the file is", uppercase)


count_vowels()
count_consonants()
count_lowercase()
count_uppercase()