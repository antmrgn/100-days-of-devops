colors_enc=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    '''look up the numerical value associated with a particular color band'''
    for i, col in enumerate(colors_enc):
        if col == color:
            return i

def value(colors):
    '''take color names as input and output a two digit number, even if the input is more than two colors'''
    return int(str(color_code(colors[0])) + str(color_code(colors[1])))
