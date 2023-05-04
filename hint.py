import clean
import math
import Wordle175
# drawing the frequency table of the whole file
def frequency_table():

    frequency_data_list = clean.words_sort()   # getting the list of words from the clean file
    word_string = ''.join(frequency_data_list)   # combining the whole list and making it a string
    total = len(word_string)     #  getting the total length of word
    alphabets = "abcdefghijklmnopqrstuvwxyz"      # accessing all alphabets to access the dictionaries
    freq_dict = {'a': 0,'b': 0,'c' : 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0}
    # making a dictionary to store the coount of all alphabets

    for i in range(len(alphabets)):
        count = word_string.count(alphabets[i])  # counting the no of occurences in the string of words
        freq_dict[alphabets[i]] = count          # storing  the value of count inn the dictionary

        relative_freq = round(((freq_dict[alphabets[i]]*100)/total),2)  # calculating the relative frequency
        histogram = math.floor(relative_freq)   # rounding the integer to the number

        print(f"{alphabets[i].upper(): <5} : {freq_dict[alphabets[i]]: <5}  {relative_freq: <5} {'*'*histogram} ")      # drawing the histogram

class Template1 (Wordle175.ScrabbleDict):
    def __init__(self):
        self.template_list = clean.words_sort()      # getting the list of words from clean file


    def getMaskedWords(self,Template) :      # this function is  returning the list oof words that follow the template
        index_list = Template[0]          # Template consist of two list one is green list and the other one is index_list
        green_list = Template[1]
        self.green_list = green_list
        self.template_list_words = []
        for i in range(len(self.template_list)) :         # Iterating over each and every word in the file and checking whether the word follows the template or not
            check_letter_sum = 0                      # counting the number of letter that the word contain and which are also in random word at correct place
            for j in range(len(self.template_list[i])):
                for k in range(len(green_list)) :
                    if index_list[k] == j and green_list[k][0].lower() == self.template_list[i][j]:     # checking the conditions whether the letter is present and at correct place or not
                        check_letter_sum += 1  # if the condition is satisfied then increasing the count
                        if check_letter_sum == len(green_list):     # checking whether the count is equall to the length of the green list or not
                            self.template_list_words.append(self.template_list[i])         # if yes then apppending that word in the template_list
        return self.template_list_words


    def getConstrainedWords(self,Template, letter):
        Constraint_Template = []
        self.Not_index = Template[2]
        for word in self.template_list_words :
            for j in self.Not_index :
                if word[j] == letter :
                    Constraint_Template.append(word)
                    break
        return Constraint_Template






if __name__ == "__main__":
    frequency_table()
    letter2 = 'a'
    object1 = Template(letter2)
    object1()

