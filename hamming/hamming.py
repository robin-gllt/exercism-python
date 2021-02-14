def distance(strand_a: str, strand_b: str):
    
    if len(strand_a) != len(strand_b):
        raise ValueError("The two strands have different size")
    
    #Zip return list of array a combiend to b. Then we sum the iteration of a != b
    return sum(a != b for a, b in zip(strand_a, strand_b))



    ### old way
    # distance: int = 0
    # for i, letter in enumerate(strand_a):
    #     if strand_b[i] != letter:
    #         distance +=1    
    # return distance


# if __name__ == "__main__":
#     print (distance("ABCD","ABCC"))


