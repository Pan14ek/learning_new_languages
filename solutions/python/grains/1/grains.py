CHESSBOARD_SQUARES = 64

def square(number):
    if(number < 1 or number > CHESSBOARD_SQUARES):
        raise ValueError("square must be between 1 and 64")
    num_square = 1

    for i in range(1, number):
        num_square = num_square*2

    return num_square

def total():
    total_sum = 0

    for i in range(1, CHESSBOARD_SQUARES + 1):
        total_sum += square(i)

    return total_sum