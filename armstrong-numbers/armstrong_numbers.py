def is_armstrong_number(number):
    sum_digits = 0
    len_number = len(str(number))

    for digit in str(number):
        sum_digits += pow(int(digit),len_number)

    if sum_digits  == number:
        return True
    else:
        return False
