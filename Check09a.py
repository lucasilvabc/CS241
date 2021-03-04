def main():
    while True:
        try:
            n = input("Please enter an integer: ")
            n = int(n)
            break
        except ValueError:print("Not a valid integer, please try again.")
 
    print("Successfully entered an integer.") 
    
if __name__ == "__main__":
    main()

