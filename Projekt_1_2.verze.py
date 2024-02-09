
###projekt_1.py: První projekt - Textový analyzátor
###author: Eliška Matějková
###email: elinka.elis.111@gmail.com
###discord: eliskamatejkova_72569

from task_template import TEXTS

from user_password import users

num_texts = int(len(TEXTS))

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
        print(f"We have {num_texts} texts to be analyzed.", sep="\n")

print(separator)

text_number = str(input(f"Enter a number btw. 1 and {num_texts} to select:"))

print(separator)

if      text_number.isalpha():
        print("The answer does not contain any number listed in the menu.",
        "Terminating the program..")
        quit()

elif    text_number.isdigit() and not int(text_number) in list(range(1, num_texts + 1)):
        print("This text number is not in the menu. Terminating the program.")
        quit()

elif    text_number.isdigit() and int(text_number) in list(range(1, num_texts + 1)):
            
        text_to_analyse = []

        for word in TEXTS[int(text_number) - 1].split():
            clean_word = word.strip(",.:;'")
            text_to_analyse.append(clean_word)

        word_count = len(text_to_analyse)
        print(f"There are {word_count} words in the selected text.")

        title_case = {}
        for i, text in enumerate([text_to_analyse]):
            print(f"There are {len([word for word in text_to_analyse if word.istitle()])} words in the selected text.")

        upper_case_words = {}
        for i, text in enumerate([text_to_analyse]):
            print(f"There are {len([word for word in text_to_analyse if word.isupper() and word.isalpha()])} uppercase words.")

        lowercase_words = {}
        for i, text in enumerate([text_to_analyse]):
            print(f"There are {len([word for word in text_to_analyse if word.islower()])} lowercase words.")

        numeric_strings = {}
        for i, text in enumerate([text_to_analyse]):
            print(f"There are {len([word for word in text_to_analyse if word.isdigit()])} numeric strings.")

        numbers = []
        for number in text_to_analyse:
            if number.isdigit():
                numbers.append(int(number))
        total_sum = sum(numbers)
        print(f"The sum of all the numbers {total_sum}.") 

print(separator)

word_lengths = [len(word) for word in text_to_analyse]

frequency = {length: word_lengths.count(length) for length in set(word_lengths)}

print(f"LEN|    OCCURENCES    |NR.")

print(separator)

for length, count in sorted(frequency.items()):
    print("{:3d}|{:18}|{:1d}".format(length, "*"*count, count))
