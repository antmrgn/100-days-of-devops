colors_enc=['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

def color_code(color):
    '''look up the numerical value associated with a particular color band'''
    for i, col in enumerate(colors_enc):
        if col == color:
            return i


def colors():
    '''list the different band colors'''
    return colors_enc
