def leap_year(year):

    if year % 4 == 0:
        if year % 400 ==0:
            return True
        elif year % 100 == 0:
            return False
        return True
    else:
        return False

# if __name__ == '__main__':
#     print(leap_year(2000))


