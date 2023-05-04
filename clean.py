def clean_file():
    # open file for reading purpose
    file=open("word5Dict.txt","r")
    # open file for writing purpose
    new_file=open("Words5Dict.txt","w")
    file_contents=file.readlines()
    def write(word_list):
        '''function to write lines in file
           Input:list
           Output:None
        '''
        for word in word_list:
            word=word.strip() # to remove'\n'
            if len(word)!=0:
                new_file.write(word+"\n")

    # iterate throigh everyline
    for line in file_contents:
        word_list=(line.split("#")) # split the line into words
        # write each word in file
        write(word_list)
    new_file.close()