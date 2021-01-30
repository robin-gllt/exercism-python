def square(number):
    if number <= 0 or number > 64:
        raise ValueError("Invalid number")

    return int(pow(2,number) / 2)

def total():
    return int(pow(2,64)) - 1



# if __name__ == "__main__":
#     print (square(64))
#     print (total())