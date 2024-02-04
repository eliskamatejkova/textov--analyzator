
###projekt_1.py: První projekt - Textový analyzátor
###author: Eliška Matějková
###email: elinka.elis.111@gmail.com
###discord: eliskamatejkova_72569

##Text:

TEXTS = {
"1": '''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
"2": '''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
"3": '''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
}

number_of_texts = list(TEXTS.keys())[2]

##Statistics - Text n.1:

#number of words in the text

clean_words_1 = []

for word_1 in TEXTS["1"].split():
    clean_word_1 = word_1.strip(",.:;'")
    clean_words_1.append(clean_word_1)

words_number_1 = len(clean_words_1)

#number of words starting with a capital

capital_words_1 = []

for capital_word_1 in clean_words_1:
    if  capital_word_1.istitle():
        capital_words_1.append(capital_word_1)

words_number_capital_1 = len(capital_words_1)

#number of words composed only of capitals

uppercase_words_1 = []

for uppercase_word_1 in clean_words_1:
    if  uppercase_word_1.isupper() and uppercase_word_1.isalpha():   
        uppercase_words_1.append(uppercase_word_1)

words_number_uppercase_1 = len(uppercase_words_1)

#words composed only of lowercase letters

lowercase_words_1 = []

for lowercase_word_1 in clean_words_1:
    if  lowercase_word_1.islower():   
        lowercase_words_1.append(lowercase_word_1)

words_number_lowercase_1 = len(lowercase_words_1)

#how many numbers in the text

numbers_1 = []

for number_1 in clean_words_1:
    if  number_1.isdigit():   
        numbers_1.append(number_1)

count_numbers_1 = len(numbers_1)

#sum of all numbers in the text

int_numbers_1 = []

int_numbers_1 = [int(int_number_1) for int_number_1 in numbers_1]

sum_numbers_1 = sum(int_numbers_1)

#frequency of different word lengths in the text

word_lengths_1 = list()

for word_length_1 in clean_words_1:
    word_lengths_1.append(len(word_length_1))
    word_lengths_1.sort()

frequency_lengths_1 = {}

for lenght_1 in word_lengths_1: 
    if  lenght_1 not in frequency_lengths_1:
        frequency_lengths_1[lenght_1] = 1
    else:
        frequency_lengths_1[lenght_1] = frequency_lengths_1[lenght_1] + 1

keys_1 = list(frequency_lengths_1.keys())


##Statistics - Text n.2:

#number of words in the text

clean_words_2 = []

for word_2 in TEXTS["2"].split():
    clean_word_2 = word_2.strip(",.:;'")
    clean_words_2.append(clean_word_2)

words_number_2 = len(clean_words_2)

#number of words starting with a capital

capital_words_2 = []

for capital_word_2 in clean_words_2:
    if  capital_word_2.istitle():
        capital_words_2.append(capital_word_2)

words_number_capital_2 = len(capital_words_2)

#number of words composed only of capitals

uppercase_words_2 = []

for uppercase_word_2 in clean_words_2:
    if  uppercase_word_2.isupper() and uppercase_word_2.isalpha():   
        uppercase_words_2.append(uppercase_word_2)

words_number_uppercase_2 = len(uppercase_words_2)

#words composed only of lowercase letters

lowercase_words_2 = []

for lowercase_word_2 in clean_words_2:
    if  lowercase_word_2.islower():   
        lowercase_words_2.append(lowercase_word_2)

words_number_lowercase_2 = len(lowercase_words_2)

#how many numbers in the text 

numbers_2 = []

for number_2 in clean_words_2:
    if  number_2.isdigit():   
        numbers_2.append(number_2)

count_numbers_2 = len(numbers_2)

#sum of all numbers in the text

int_numbers_2 = []

int_numbers_2 = [int(int_number_2) for int_number_2 in numbers_2]

sum_numbers_2 = sum(int_numbers_2)

#frequency of different word lengths in the text

word_lengths_2 = list()

for word_length_2 in clean_words_2:
    word_lengths_2.append(len(word_length_2))
    word_lengths_2.sort()

frequency_lengths_2 = {}

for lenght_2 in word_lengths_2: 
    if  lenght_2 not in frequency_lengths_2:
        frequency_lengths_2[lenght_2] = 1
    else:
        frequency_lengths_2[lenght_2] = frequency_lengths_2[lenght_2] + 1

keys_2 = list(frequency_lengths_2.keys())


##Statistics - Text n.3:

#number of words in the text

clean_words_3 = []

for word_3 in TEXTS["3"].split():
    clean_word_3 = word_3.strip(",.:;'")
    clean_words_3.append(clean_word_3)

words_number_3 = len(clean_words_3)

#number of words starting with a capital

capital_words_3 = []

for capital_word_3 in clean_words_3:
    if  capital_word_3.istitle():
        capital_words_3.append(capital_word_3)

words_number_capital_3 = len(capital_words_3)

#number of words composed only of capitals

uppercase_words_3 = []

for uppercase_word_3 in clean_words_3:
    if  uppercase_word_3.isupper() and uppercase_word_3.isalpha():   
        uppercase_words_3.append(uppercase_word_3)

words_number_uppercase_3 = len(uppercase_words_3) 

#words composed only of lowercase letters

lowercase_words_3 = []

for lowercase_word_3 in clean_words_3:
    if  lowercase_word_3.islower():   
        lowercase_words_3.append(lowercase_word_3)

words_number_lowercase_3 = len(lowercase_words_3)

#how many numbers in the text 

numbers_3 = []

for number_3 in clean_words_3:
    if  number_3.isdigit():   
        numbers_3.append(number_3)

count_numbers_3 = len(numbers_3)

#sum of all numbers in the text

int_numbers_3 = []

int_numbers_3 = [int(int_number_3) for int_number_3 in numbers_3]

sum_numbers_3 = sum(int_numbers_3)

#frequency of different word lengths in the text

word_lengths_3 = list()

for word_length_3 in clean_words_3:
    word_lengths_3.append(len(word_length_3))
    word_lengths_3.sort()

frequency_lengths_3 = {}

for lenght_3 in word_lengths_3: 
    if  lenght_3 not in frequency_lengths_3:
        frequency_lengths_3[lenght_3] = 1
    else:
        frequency_lengths_3[lenght_3] = frequency_lengths_3[lenght_3] + 1

keys_3 = list(frequency_lengths_3.keys())


##Users:

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

##Program:

separator = "-" * 40

user = input("Enter your username:")

if      not user in users:
        print("Unregistered user. Terminating the program..")
        quit()

elif    user in users:
        password = input("Enter your password:") 

print(separator)

if      user in users and users.get(user) != password:
        print("Wrong password. Terminating the program..")
        quit()

elif    user in users and users.get(user) == password:
        print(f"Welcome to the app, {user}.")
        print(f"We have {number_of_texts} texts to be analyzed.", sep="\n")

print(separator)

text_number = str(input("Enter a number btw. 1 and 3 to select:"))

print(separator)

if      text_number.isdigit() and text_number in TEXTS and text_number == "1":
        print(f"There are {words_number_1} words in the selected text.")
        print(f"There are {words_number_capital_1} titlecase words.")
        print(f"There are {words_number_uppercase_1} uppercase words.")
        print(f"There are {words_number_lowercase_1} lowercase words.")
        print(f"There are {count_numbers_1} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers_1}.")

elif    text_number.isdigit() and text_number in TEXTS and text_number == "2":
        print(f"There are {words_number_2} words in the selected text.")
        print(f"There are {words_number_capital_2} titlecase words.")
        print(f"There are {words_number_uppercase_2} uppercase words.")
        print(f"There are {words_number_lowercase_2} lowercase words.")
        print(f"There are {count_numbers_2} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers_2}.")

elif    text_number.isdigit() and text_number in TEXTS and text_number == "3":
        print(f"There are {words_number_3} words in the selected text.")
        print(f"There are {words_number_capital_3} titlecase words.")
        print(f"There are {words_number_uppercase_3} uppercase words.")
        print(f"There are {words_number_lowercase_3} lowercase words.")
        print(f"There are {count_numbers_3} numeric strings.")
        print(f"The sum of all the numbers {sum_numbers_3}.")

elif    text_number.isdigit() and not text_number in TEXTS:
        print("This text number is not in the menu. Terminating the program.")
        quit()

else:
        print("The answer does not contain any number listed in the menu.", 
              "Terminating the program..")
        quit()

print(separator)


if      text_number == "1":
        print(f"len |  occurences  | nr.".upper())
        print(separator)
        print(keys_1[0], " ", "|", "*" * frequency_lengths_1.get(1),
        "|".rjust(12), frequency_lengths_1.get(1))
        print(keys_1[1], " ", "|", "*" * frequency_lengths_1.get(2),
        "|".rjust(4), frequency_lengths_1.get(2))
        print(keys_1[2], " ", "|", "*" * frequency_lengths_1.get(3),
        "|".rjust(7), frequency_lengths_1.get(3))
        print(keys_1[3], " ", "|", "*" * frequency_lengths_1.get(4),
        "|".rjust(2), frequency_lengths_1.get(4))
        print(keys_1[4], " ", "|", "*" * frequency_lengths_1.get(5),
        "|".rjust(1), frequency_lengths_1.get(5))
        print(keys_1[5], " ", "|", "*" * frequency_lengths_1.get(6),
        "|".rjust(10), frequency_lengths_1.get(6))
        print(keys_1[6], " ", "|", "*" * frequency_lengths_1.get(7),
        "|".rjust(9), frequency_lengths_1.get(7))
        print(keys_1[7], " ", "|", "*" * frequency_lengths_1.get(8),
        "|".rjust(8), frequency_lengths_1.get(8))
        print(keys_1[8], " ", "|", "*" * frequency_lengths_1.get(9),
        "|".rjust(12), frequency_lengths_1.get(9))
        print(keys_1[9], "", "|", "*" * frequency_lengths_1.get(10),
        "|".rjust(12), frequency_lengths_1.get(10))
        print(keys_1[10], "", "|", "*" * frequency_lengths_1.get(11),
        "|".rjust(12), frequency_lengths_1.get(11))

elif    text_number == "2":
        print(f"len |     occurences     | nr.".upper())
        print(separator)
        print(keys_2[0], " ", "|", "*" * frequency_lengths_2.get(2),
        "|".rjust(12), frequency_lengths_2.get(2))
        print(keys_2[1], " ", "|", "*" * frequency_lengths_2.get(3),
        "|".rjust(2), frequency_lengths_2.get(3))
        print(keys_2[2], " ", "|", "*" * frequency_lengths_2.get(4),
        "|".rjust(10), frequency_lengths_2.get(4))
        print(keys_2[3], " ", "|", "*" * frequency_lengths_2.get(5),
        "|".rjust(9), frequency_lengths_2.get(5))
        print(keys_2[4], " ", "|", "*" * frequency_lengths_2.get(6),
        "|".rjust(12), frequency_lengths_2.get(6))
        print(keys_2[5], " ", "|", "*" * frequency_lengths_2.get(7),
        "|".rjust(16), frequency_lengths_2.get(7))
        print(keys_2[6], " ", "|", "*" * frequency_lengths_2.get(8),
        "|".rjust(17), frequency_lengths_2.get(8))
        print(keys_2[7], " ", "|", "*" * frequency_lengths_2.get(9),
        "|".rjust(14), frequency_lengths_2.get(9))
        print(keys_2[8], "", "|", "*" * frequency_lengths_2.get(10),
        "|".rjust(18), frequency_lengths_2.get(10))
        print(keys_2[9], "", "|", "*" * frequency_lengths_2.get(13),
        "|".rjust(18), frequency_lengths_2.get(13))
        
elif    text_number == "3":
        print(f"len |    occurences    | nr.".upper())
        print(separator)
        print(keys_3[0], " ", "|", "*" * frequency_lengths_3.get(1),
        "|".rjust(16), frequency_lengths_3.get(1))
        print(keys_3[1], " ", "|", "*" * frequency_lengths_3.get(2),
        "|".rjust(6), frequency_lengths_3.get(2))
        print(keys_3[2], " ", "|", "*" * frequency_lengths_3.get(3),
        "|".rjust(2), frequency_lengths_3.get(3))
        print(keys_3[3], " ", "|", "*" * frequency_lengths_3.get(4),
        "|".rjust(8), frequency_lengths_3.get(4))
        print(keys_3[4], " ", "|", "*" * frequency_lengths_3.get(5),
        "|".rjust(7), frequency_lengths_3.get(5))
        print(keys_3[5], " ", "|", "*" * frequency_lengths_3.get(6),
        "|".rjust(12), frequency_lengths_3.get(6))
        print(keys_3[6], " ", "|", "*" * frequency_lengths_3.get(7),
        "|".rjust(6), frequency_lengths_3.get(7))
        print(keys_3[7], " ", "|", "*" * frequency_lengths_3.get(8),
        "|".rjust(11), frequency_lengths_3.get(8))
        print(keys_3[8], " ", "|", "*" * frequency_lengths_3.get(9),
        "|".rjust(14), frequency_lengths_3.get(9))
        print(keys_3[9], "", "|", "*" * frequency_lengths_3.get(10),
        "|".rjust(14), frequency_lengths_3.get(10))
                                                                            
