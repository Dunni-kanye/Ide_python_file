from operator import truediv


def biggest_odd_number(number: str):
    biggest_number = 0
    for numbers  in number:
        numbers = int(numbers)
        if numbers > biggest_number and numbers % 2 != 0:
            biggest_number = numbers
    return biggest_number

#iggest_odd_number("23456780")

def equal_strings(first_number:str, second_number:str):
    count = ""
    if len(first_number) == len(second_number):
        for index in second_number:
            if index in first_number: count += index
        if len(count)== len(second_number): return True
        else: return False
    else: return False








