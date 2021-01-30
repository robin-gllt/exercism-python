def distance(strand_a, strand_b):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("The two strands have different size")
    
    if strand_a == strand_b:  #not sure how costly in term of resources is this, verification is also done later via the for loop
        return 0

    distance = 0

    for i, letter in enumerate(strand_a):
        if strand_b[i] != letter:
            distance +=1    

    return distance


if __name__ == "__main__":
    print (distance("ABC","ABC"))


