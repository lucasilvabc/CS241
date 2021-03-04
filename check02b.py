def my_file():
    filename = input("Enter file: ")
    return filename
    
def read_file(filename):
    line_count = 0
    word_count = 0
    with open(filename, "r") as file_in:
        for line in file_in:
            line_count += 1
            words = line.split()
            word_count += len(words)
        return (word_count, line_count)

def main():
    filename = my_file()
    (word_count, line_count) = read_file(filename)
    print ("The file contains {} lines and {} words.".format(line_count,word_count))

if __name__ == "__main__":
    main()           

