__version__="0.0.1"

dcolor="1"

def indeterminate():
    print("\x1b]9;4;3\x1b\\",end="",flush=True)

def show(value:int,color:str=None):
    global dcolor
    if(color!=None):
        color={"green":1,"g":1,"red":2,"r":2,"yellow":4,"y":4}[color]
        dcolor=color
    else:
        color=dcolor
    value=int(value)
    print("\x1b]9;4;{};{}\x1b\\".format(color,value),end="",flush=True)

def close():
    print("\x1b]9;4;0\x1b\\",end="",flush=True)
