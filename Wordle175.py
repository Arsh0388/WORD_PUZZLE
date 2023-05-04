import clean

class ScrabbleDict :
    def __init__(self,size,filename) :
        self.filename = filename
        self.size = size          # initalizing the size and keys of dictionaries
        dict1 = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}
        self.dict1 = dict1
        file_read = clean.words_sort()   # getting the list of words from clean filee word_sort() function from the clean file

        for each_word in file_read :
            if each_word.isalpha() == True :
                self.dict1[each_word[0]].append(each_word)    # placing each word in the dictionary according the letter

    def check(self, word):    # checking whether the input word is in the dictionary or not with its first letter
        self.word = word
        if word in self.dict1[word[0]]:     # checking the word in thedictionary starting with first letter of word
            return True
        else:
            return False

    def getSize(self):
        dict_size = 0
        for i in self.dict1:
            dict_size += len(self.dict1[i])     # getting the size of the dictionary 
        return dict_size

    def getWords(self,letter) :       # getting the list of words starting with the correct letter
        return self.dict1[letter]

    def getWordSize(self):
        dict_words_size =  []
        for key_list in self.dict1 :
            for WORDS in key_list :
                dict_words_size.append(len())

if __name__ == "__main__":
    filename = "scrabble5.txt"
    size = 26
    obj = ScrabbleDict(size,filename)        # calling the class

    Correctness = obj.check('hello')   # checking whether the word hello exist in the dictionary or not
    print(Correctness)            # printing the value of Correctness True/False







