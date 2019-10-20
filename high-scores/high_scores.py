def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]



# if __name__ == "__main__":
#   print (personal_top_three([10,5,2,6]))


