def steps(number):
    if number == 0 or number < 0:
        raise ValueError("Only positive integers are allowed")
    return stepCounter(0, number)
    
def stepCounter(step, number):
    if number == 1:
        return step
    elif number % 2 == 0:
        return stepCounter(step + 1,number // 2)
    else:
        return stepCounter(step + 1, number * 3 + 1)
