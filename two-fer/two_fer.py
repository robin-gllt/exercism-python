def two_fer(name=""):
    if name == "" :
        return "One for you, one for me."
    else:
        return "One for " + str(name) + ", one for me."


if __name__ == '__main__':
    print("Example:")
    print(two_fer())
