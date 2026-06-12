"""Functions to automate Conda airlines ticketing system."""


def generate_seat_letters(number):
    """Generate a series of letters for airline seats.

    Parameters:
        number (int): Total number of seat letters to be generated.

    Returns:
        generator: A generator that yields seat letters.

    Note:
        Seat letters are generated from A to D.
        After D the sequence starts again with A.
        For example: A, B, C, D, A, B

    """
    seat_letters = ["A", "B", "C", "D"]

    for num in range(number):
        yield seat_letters[num % len(seat_letters)]


def generate_seats(number):
    """Generate a series of identifiers for airline seats.

    Parameters:
        number (int): The total number of seats to be generated.

    Returns:
        generator: A generator that yields seat numbers.

    Note:
        A seat number consists of the row number and the seat letter.
        There is no row 13, and each row has 4 seats.

        Seats should be sorted from low to high.
        For example: 3C, 3D, 4A, 4B

    """

    letters = ["A", "B", "C", "D"]

    for i in range(number):
        row = i // 4 + 1

        if row >= 13:
            row += 1
        
        letter = letters[i % len(letters)]
        yield str(row) + letter


def assign_seats(passengers):
    """Assign seats to passengers.

    Parameters:
        passengers (list[str]): A list of strings containing names of passengers.

    Returns:
        dict: With passenger names as keys and seat numbers as values.
        Example output: {"Adele": "1A", "Björk": "1B"}

    """
    seats = generate_seats(len(passengers))

    passenger_seats = dict()

    for passenger in passengers:
        passenger_seats[passenger] = next(seats)

    return passenger_seats


def generate_codes(seat_numbers, flight_id):
    """Generate codes for a ticket.

    Parameters:
        seat_numbers (list[str]): A list of seat numbers.
        flight_id (str): A string containing the flight identifier.

    Returns:
        generator: A generator that yields 12 character long ticket codes.

    """

    total_flight_ticket_letters = 12
    
    for seat_number in seat_numbers:
        currrent_ticket_letters = len(seat_number + flight_id)
        letters_need_to_add = total_flight_ticket_letters - currrent_ticket_letters
        
        yield seat_number + flight_id + (str(0) * letters_need_to_add)
