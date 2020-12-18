import sys


# Print the launch menu for user selection
def print_menu():
    print("What would you like to do?")
    print("1: Get the score of a word")
    print("2: Get the average score of words in a file")
    print("3: Find the highest / lowest scoring words in a file")
    print("4: Sort the words in a file into positive.txt and negative.txt")
    print("5: Exit the program")


# Remove non alphabetic characters from a list of strings
def no_punc(lines):
    for i in range(0, len(lines)):
        lines[i] = ''.join(letter for letter in lines[i] if ord('a') <= ord(letter) <= ord('z'))
    return lines


# Create sentiments/counts dictionaries from learning data file
def create_dicts():
    while True:
        file_name = input("Learning data file name? ")
        try:
            f = open(file_name, "r")
        except FileNotFoundError or ValueError:
            print("Invalid file input!!")
            continue
        break

    count = dict()
    sentiment = dict()
    for line in f:
        line = line.strip().lower()
        words = line.split()
        words = no_punc(words)
        score = float(line.split()[0])

        for word in words:
            if word == '':
                continue
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

            if word not in sentiment:
                sentiment[word] = score
            else:
                sentiment[word] += score

    for i in sentiment.keys():
        sentiment[i] = round(sentiment[i] / count[i], 2)

    f.close()
    return sentiment, count


# print score of a word/string and its connotation.
def print_category(score, word):
    print("score", "=", score)
    print(word, end=" ")
    if score > 2.01:
        print("is positive")
    elif score < 1.99:
        print("is negative")
    else:
        print("is neutral")


# Get/return user input from menu displayed by print_menu()
def print_prompt():
    while True:
        print_menu()
        try:
            num_input = int(input("Enter a number 1 - 5: "))
        except ValueError:
            print("Incorrect input!")
            continue

        if 1 <= num_input <= 5:
            break
        else:
            print("Incorrect input!")

    return num_input


# adds a score and word(s) to the provided sentiment/count dictionaries to further train the program
def add(score, words, sentiments, counts):
    split_words = list(words)
    for word in split_words:
        if word not in sentiments.keys():
            sentiments[word] = score
            counts[word] = 1
        else:
            counts[word] += 1
            sentiments[word] = (sentiments[word] * counts[word] + score) / counts[word]


# Displays the average score of entire file
def file_avg(sentiments, counts):
    avg = 0
    num_val = 0

    file_input = input("file name? ")
    try:
        file = open(file_input, "r")
        file_str = file.read()
        file_list = file_str.split()
    except FileNotFoundError:
        print("File does not exist!")

    for line in file_list:
        line = line.lower()
        line = line.strip()
        words = line.split()
        words = no_punc(words)

        for word in words:
            if word in sentiments:
                avg += sentiments[word]
                num_val += 1

    avg = round(avg / num_val, 2)
    print_category(avg, file_str)

    usr_input = input("Am I right (yes/no)? ")
    if usr_input.lower() == "no":
        try:
            num_input = int(input("noWhat score should this sentence have (0 - 4 where 4 is the most positive)? "))
        except ValueError:
            print("Invalid input!")

        add(num_input, file_str, sentiments, counts)
    file.close()


# Displays max/min scored words from provided file
def min_max(sentiments, counts):
    file_dict = dict()
    file_input = input("file name? ")
    try:
        file = open(file_input, "r")
    except FileNotFoundError:
        print("File does not exist!")

    for line in file:
        line = line.lower()
        line = line.strip()
        words = line.split()
        words = no_punc(words)

        for word in words:
            if word in sentiments.keys():
                file_dict[word] = sentiments[word]

    maximum = max(file_dict, key=file_dict.get)
    minimum = min(file_dict, key=file_dict.get)
    print("Maximum score is", file_dict[maximum], "for", maximum)
    print("Minimum score is", file_dict[minimum], "for", minimum)
    file.close()


# Client program
def main():
    POSITIVE_FILE = "positives.txt"
    NEGATIVE_FILE = "negatives.txt"
    sentiments, counts = create_dicts()

    while True:
        usr_input = print_prompt()

        if usr_input == 5:
            sys.exit()

        if usr_input == 1:
            word_input = input("which word? ")

            if word_input not in sentiments.keys():
                continue
            print_category(sentiments[word_input], word_input)

        elif usr_input == 2:
            file_avg(sentiments, counts)

        elif usr_input == 3:
            min_max(sentiments, counts)

        elif usr_input == 4:
            pos = open(POSITIVE_FILE, "w")
            neg = open(NEGATIVE_FILE, "w")
            for word in sentiments.keys():
                if sentiments[word] > 2.01:
                    pos.write(word + ' = ' + str(sentiments[word]) + '\n')
                elif sentiments[word] < 1.99:
                    neg.write(word + ' = ' + str(sentiments[word]) + '\n')

            pos.close()
            neg.close()

        print()


if __name__ == "__main__":
    main()