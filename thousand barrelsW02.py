def prompt_filename():
    fileName= input("Enter a file: ")
    return fileName
​
def parse_file(file_name, word):
    textFile= open(file_name,'r')
    new_word = word.lower()
    count_word=0
    for line in textFile:
        words = line.split()
        for i in words:
            x = i.lower()
            letter_count = 0
            index = 0
            for letter in new_word:
                if len(x) < len(new_word):
                    pass
                elif letter == x[index]:
                    letter_count+=1 
                index += 1
            if letter_count == len(new_word):
                count_word += 1
                print(x)
            #if x == new_word:
                #count_word+=1
    return count_word
​
def main():
    fileName= prompt_filename()
    print("Opening file",fileName)
    word = input("Enter a word: ")
    numOccurs = parse_file(fileName, word)
    print("The word",word,"occurs",numOccurs,"times in this file.")
​
if __name__ == "__main__":
    main()

