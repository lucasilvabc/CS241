def prompt_file():
    file_name = input("Please enter the data file: ")
    open_file = open(file_name, 'r')
    the_file = open_file.readlines()
    open_file.close()
    del(the_file[0]) #The first line was skipped
    return(the_file)


'''This function will calculate the average commercial'''
def average_file(file_default):
    average_sum = 0
    average = 0
    for line in file_default:
        datas = line.split(',')
        average_sum += float(datas[6])
    average = average_sum/len(file_default)
    print("\nThe average commercial rate is:", average) 


'''This function will show the highest rate'''
def highest(file_default):
    bigger_line = [0]*9
    for line in file_default:
        datas = line.split(',')
        if float(datas[6]) > float(bigger_line[6]): #Float is used to define exactly the value
            bigger_line = datas
    print("\nThe highest rate is:\n{} ({}, {}) - ${}".format(bigger_line[2],bigger_line[0],bigger_line[3],(bigger_line[6])))


'''This function will show the lowest rate'''
def lowest(file_default):
    little_line = [1]*9
    for line in file_default:
        datas = line.split(',')
        if float(datas[6]) < float(little_line[6]): #Float is used to define exactly the value
            little_line = datas
    print("\nThe lowest rate is:\n{} ({}, {}) - ${}".format(little_line[2],little_line[0],little_line[3],float(little_line[6])))        

        
'''Principal function'''
def main():
    the_file = prompt_file()   
    average = average_file(the_file)
    result_highest = highest(the_file)
    result_lowest = lowest(the_file)        
             

if __name__ == "__main__":
    main()              