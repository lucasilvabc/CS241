def prompt_number():
    num = int(input("Enter a positive number: "))
    
    while num < 0:
        print("Invalid entry. The number must be positive.")
        num = int(input("Enter a positive number: "))
    print()
    return num    

def compute_sum(num1, num2, num3):
    return (num1 + num2 + num3)


def main():
    number1 = prompt_number()
    number2 = prompt_number()
    number3 = prompt_number()
    sum = compute_sum(number1, number2, number3)
    print("The sum is:", str(sum))

if __name__ == "__main__":
    main()