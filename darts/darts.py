import math

def score(x, y):
    rayon = math.sqrt(x**2+y**2)
    
    if rayon > 10:
        return 0
    elif rayon > 5:
        return 1
    elif rayon > 1:
        return 5
    elif rayon > 0:
        return 10
  

if __name__ == "__main__":
  print(score(11,2))
  


