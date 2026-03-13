# args = arguments

def fun(*args):
    return sum(args)

print(fun(5, 10, 15))

# k = keyword
# val = value
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

# argv = argument values
def myfun(*argv):
    for arg in argv:
        print(arg)

myfun("Hello", "World", "!!!!!!")

def mult(*args):
    res = 1
    for num in args:
        res *= num

    return res

print(mult(2 , 10 , 2))

# can pass any number of arguments in the key=value

def vfun(**kwargs):
    for k, val in kwargs.items():
        print(k,'=', val)

vfun(a1='This', a2='Is', a3='Gr8', a4='Mate')

def introduce(**kwargs):
    deets = []
    for k,v in kwargs.items():
        deets.append(k + ':' + str(v))
    return ", ".join(deets)

print(introduce(Name="Fari", Age="28", City="San Juan"))

def faveGames(*args, **kwargs):
    print("Games:", args)
    print("Title:", kwargs)

faveGames(
    "Zelda", "Metroid", "Kingdom Hearts", Zelda='Majoras Mask'
    , Metroid='Prime', KingdomHearts='II' )

