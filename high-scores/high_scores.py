def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    scores.sort()
    if len(scores) > 2:
      return [scores[-1], scores[-2], scores[-3]]
    elif len(scores) > 1 : 
      return [scores[-1], scores[-2]]
    else:
      return [scores[-1]]


# if __name__ == "__main__":
#   print (personal_top_three([10]))


