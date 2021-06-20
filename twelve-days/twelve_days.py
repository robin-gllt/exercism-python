
# On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.
# On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.
# On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.
# # 

# DAYS = ("first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth")

# VERSES = [
#     "a Partridge in a Pear Tree.",
#     "two Turtle Doves, ",
#     "three French Hens, ",
#     "four Calling Birds, ",
#     "five Gold Rings, ",
#     "six Geese-a-Laying, ",
#     "seven Swans-a-Swimming, ",
#     "eight Maids-a-Milking, ",
#     "nine Ladies Dancing, ",
#     "ten Lords-a-Leaping, ",
#     "eleven Pipers Piping, ",
#     "twelve Drummers Drumming, "
# ]

# def recite(start_verse, end_verse):
    

#     result="On the " + DAYS[end_verse -1] + " day of Christmas my true love gave to me: "
    
#     if end_verse == 1:
#         result+= VERSES[0]
#     else:
#         for i in range (end_verse-1,-1,-1):        
#             if i == 0:
#                 result+= "and " + VERSES[0]
#             else:
#                 result+= VERSES[i]

#     return [result]

# if __name__ == "__main__":    
#     print(recite(3,3))
#     print(recite(n, n)[0] for n in range(1, 4))



twelveDict = {
1: ["first", "a Partridge in a Pear Tree."],
2: ["second", "two Turtle Doves, and a Partridge in a Pear Tree."],
3: ["third", """three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
4: ["fourth", """four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
5: ["fifth", """five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
6: ["sixth", """six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
7: ["seventh", """seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
8: ["eighth", """eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
9: ["ninth", """nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
10: ["tenth", """ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
11: ["eleventh", """eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""],
12: ["twelfth", """twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."""]}

def recite(start_verse, end_verse):
    return [f"On the {twelveDict[k][0]} day of Christmas my true love gave to me: {twelveDict[k][1]}" for k in range(start_verse, end_verse+1)]


if __name__ == "__main__":    
    print(recite(8,8))


