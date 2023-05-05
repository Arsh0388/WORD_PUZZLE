import clean
import Wordle175
import hint
import random
def main():
    Sorted_file = "Scrabble.txt"
    Sorted_Dict_Size = 26
    obj = Wordle175.ScrabbleDict(Sorted_Dict_Size,Sorted_file)
    Flag = True
    Complete_Red_List = []
    Complete_Orange_List = []
    Complete_Green_List = []
    Target_List = []
    Words_List = clean.words_sort()
    random_integer = random.randint(0,8913)
    count = 1
    random_word = Words_List[random_integer +1]
    print(random_word)
    while Flag:
        index_list = []
        red = []
        green = []
        orange = []
        guessed_word  = []
        input_word = input(f"Attempt {count} : Please enter a 5 five-letter word: ")
        variable = len(input_word)
        repeat_letter = []
        word_test = input_word
        if variable != 5:
            if variable > 5:
                print(" word is too long ")
            else:
                print(" word is too short ")

        elif input_word in guessed_word :
            print(f" {input_word.upper()} was already entered")

        elif not obj.check(input_word)  :
            print(f" {input_word.upper()} is not a recognized word")

        elif input_word == random_word:
            print(f" Found in {count} attempts. Well done. The Word is {random_word.upper()}")
            Flag = False

        elif count > 6 and input_word != random_word :
            print(f"Sorry you lose. The Word is {random_word.upper()}")
            Flag = False

        elif obj.check(input_word) :
            Target_List.append(input_word)
            count += 1
            index = 0
            for i in range(len(input_word)) :
                letter_count = (input_word.count(input_word[i]))

                if letter_count == 1:
                    if input_word[i] in random_word and input_word[i] == random_word[i] :
                        green.append(random_word[i])
                        index_list.append(i)
                    elif input_word[i] in random_word :
                            orange.append(input_word[i])
                    elif input_word[i] not in random_word:
                        red.append(input_word[i])
                else :
                    if input_word[i] not in repeat_letter :
                        index = 1
                    repeat_letter.append(input_word[i])
                    write = f"{input_word[i]}{index}"
                    if input_word[i] in random_word and  input_word[i] == random_word[i]  :
                        green.append(write)
                        index_list.append(i)

                    elif input_word[i] in random_word :
                        if input_word.count(input_word[i]) == random_word.count(random_word[i]) :
                            orange.append(write)
                    else:
                        red.append(write)
                    index += 1
            Complete_Red_List.append(red)
            Complete_Orange_List.append(orange)
            Complete_Green_List.append(green)
            print(word_test)
            for k in range(len(Target_List)):
                print(f" {Target_List[k]} Green= {Complete_Green_List[k]} - Orange= {Complete_Orange_List[k]}- Red= {Complete_Red_List[k]}")
        Template_Task = hint.Template(random_word[0])
        Template_words = Template_Task.getMaskedWords(index_list,green)
        print(Template_words)
    hint.frequency_table()

if __name__ == "__main__":
    main()






