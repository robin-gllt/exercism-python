
def color_code(color: str):
    resistor_colors = {
        "black" : 0,
        "brown" : 1 ,
        "red": 2,
        "orange" : 3,
        "yellow" :4 ,
        "green" : 5 ,
        "blue" : 6,
        "violet" : 7,
        "grey" : 8,
        "white" : 9
    }

    return (resistor_colors.get(color, "Invalid Color"))


def colors():
    return ([
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"
    ])



# if __name__ == "__main__":    
#     print (color_code("yellow"))