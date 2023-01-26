import csv
import random

def add_word(word, definition):
    with open('words.csv', mode='a') as csv_file:
        fieldnames = ['word', 'definition']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writerow({'word': word, 'definition': definition})

def quiz():
    with open('words.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        score = 0
        for row in csv_reader:
            word = row['word']
            definition = row['definition']
            choices = [definition]
            for i in range(3):
                wrong_definition = input("Enter a wrong definition for the word '" + word + "': ")
                choices.append(wrong_definition)
            random.shuffle(choices)
            print("Choose the correct definition for the word '" + word + "':")
            for i in range(4):
                print(str(i + 1) + ") " + choices[i])
            choice = input()
            if choices[int(choice) - 1] == definition:
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        print("Your score is " + str(score) + " out of " + str(csv_reader.line_num - 1) + ".")

add_word("example", "a thing characteristic of its kind or illustrating a general rule")
quiz()
