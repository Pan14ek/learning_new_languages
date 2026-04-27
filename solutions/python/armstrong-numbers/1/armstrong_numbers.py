def pow(number, power_number):
    sum = 1
    for i in range(0, power_number):
        sum *= number
    return sum

def calculate_digits(number):
    if number == 0:
        return 1
    
    count = 0

    while number != 0:
        number //= 10
        count += 1

    return count
    
def is_armstrong_number(number):
    cloned_number = number
    digits_in_number = calculate_digits(cloned_number)

    sum = 0

    while cloned_number != 0:
        divided_number = cloned_number % 10

        sum += pow(divided_number,digits_in_number)

        cloned_number//= 10

    return sum == number

