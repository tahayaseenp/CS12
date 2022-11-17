def count_vowels():
    vowels = 0
    for line in L:
        for char in line:
            if char.lower() in 'aeiou':
                vowels += 1
    print("The number of vowels in the file is", vowels)


def count_consonants():
    consonants = 0
    for line in L:
        for char in line:
            if char.isalpha() and char.lower() not in 'aeiou':
                consonants += 1
    print("The number of consonants in the file is", consonants)


def count_lowercase():
    lowercase = 0
    for line in L:
        for char in line:
            if char.islower():
                lowercase += 1
    print("The number of lowercase letters in the file is", lowercase)


def count_uppercase():
    uppercase = 0
    for line in L:
        for char in line:
            if char.isupper():
                uppercase += 1
    print("The number of uppercase letters in the file is", uppercase)


f = open("data.txt", "r")
L = f.readlines()
f.close()
count_vowels()
count_consonants()
count_lowercase()
count_uppercase()