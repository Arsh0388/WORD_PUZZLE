#----------------------------------------------------
# Assignment 2 - Class, data structure and encapsulation
# Purpose of program: wordle175 game
#
# Author: Arsh Arora
# Collaborators/references: Heena kamani in task  3
#----------------------------------------------------import clean           # importing the files that are required
import Wordle175
import hint
import random
from clean import clean_file
def main():
    Sorted_file = "Scrabble.txt"
    Sorted_Dict_Size = 26
    guessed_word  = []
    obj = Wordle175.ScrabbleDict(Sorted_Dict_Size,Sorted_file)
    Flag = True
    Complete_Red_List = []          # declaring some variables that we need
    Complete_Orange_List = []
    Complete_Green_List = []
    Target_List = []
    Words_List = clean.words_sort()     # getting the list of words from clean file which was sorted from word5Dict.txt
    random_integer = random.randint(0,8913)   # getting a random number between 0 and 8913
    count = 1       # Counting the  number of attempts
    random_word = Words_List[random_integer +1]        # Getting the word that is at that position
    print(random_word)
    while Flag:
        index_list = []
        non_index_list = []
        red = []
        green = []
        orange = []
        temp = []
        input_word = input(f"Attempt {count} : Please enter a 5 five-letter word: ")   # getting the input from the user
        input_word= input_word.lower()   # converting it to lower case
        variable = len(input_word)     # getting the length of the word
        repeat_letter = []
        if variable != 5:   # checking the length of the word
            if variable > 5:
                print(" word is too long ")
            else:
                print(" word is too short ")

        elif input_word in guessed_word :      # checking whether the word was already entered or not
            print(f" {input_word.upper()} was already entered")

        elif not obj.check(input_word)  :   # checking whether the word is valid or not
            print(f" {input_word.upper()} is not a recognized word")

        elif input_word == random_word:    # if the word is random word or not
            print(f" Found in {count} attempts. Well done. The Word is {random_word.upper()}")
            Flag = False

        elif count > 6 and input_word != random_word :  # if count is greater than quitting the game
            print(f"Sorry you lose. The Word is {random_word.upper()}")
            Flag = False

        elif obj.check(input_word) :
            Target_List.append(input_word)
            count += 1       # counting the number of attemnps and increasing the
            index = 1
            for i in range(len(input_word)) :
                letter_count = (input_word.count(input_word[i]))     # counting the number of times the  letter is cokinng in the word

                if letter_count == 1:
                    if input_word[i] in random_word and input_word[i] == random_word[i] :
                        green.append(random_word[i].upper())          # if the letter  is presennt and at ccorrect place then appending it in the green list
                        index_list.append(i)       # getting the index of the letter

                    elif input_word[i] in random_word :
                            orange.append(input_word[i].upper())  # if letter is present and at wrong place appending it in the orange list

                            non_index_list.append(i)
                    elif input_word[i] not in random_word:
                        red.append(input_word[i].upper()) # if letter is not present  then in the red list

                        non_index_list.append(i)
                else :
                    if input_word[i] not in repeat_letter:      # doing same for the letters that are repeating
                        index = 1
                    repeat_letter.append(input_word[i])
                    write = f"{input_word[i]}{index}"
                    if input_word[i] in random_word and  input_word[i] == random_word[i]  :
                        green.append(write.upper())     # if the letter is present then appending it in the green list
                        index_list.append(i)
                        non_index_list.append(i)

                    elif (input_word[i] in random_word) and (input_word.count(input_word[i]) == random_word.count(input_word[i]) or input_word.count(input_word[i]) < random_word.count(input_word[i]) ) :
                        orange.append(write.upper())
                        non_index_list.append(i)
                    elif input_word[i] in random_word or input_word[i] not in random_word:
                        red.append(write.upper())
                        non_index_list.append(i)
                    index += 1
            Complete_Red_List.append(red)          # storing all green orange and red list of a word
            Complete_Orange_List.append(orange)
            Complete_Green_List.append(green)


            for k in range(len(Target_List)):
                print(f" {Target_List[k]} Green= {sorted(Complete_Green_List[k])} - Orange= {sorted(Complete_Orange_List[k])}- Red= {sorted(Complete_Red_List[k])}")
            Template = []
            Template.append(index_list)   # storing the index and green list in the Template
            Template.append(green)
            Template.append(non_index_list)
            template_request = input(" you want to get the template or not yes/no ") # asking for the template request
            if len(green) != 0:
                if template_request == "yes" :
                    Template_Task = hint.Template1()  # calling the Template class
                    Template_words = Template_Task.getMaskedWords(Template)
                    print(Template_words)    # printing the words that follow the template
                    template_letter = input(" enter the template letter ")  # asking for an additional letter
                    Constraint_Task = []
                    Constraint_Task = Template_Task.getConstrainedWords(Template, template_letter)
                    print(Constraint_Task)

        guessed_word.append(input_word)
    hint.frequency_table()          # calling the function that draws the frequency table

if __name__ == "__main__":
    main()
    # task 4 constrained words is not working properly for repeat letters

