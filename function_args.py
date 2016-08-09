#function arguments can be specifed with defaults

# but default argument expressions evaluated only once,when def is executed
# so output will be  devil,devil,devil
# to get it only once don't specify list in function arguments instead specify none

def add_devil(menu=[]):
    menu.append('devilll')
    return menu

def add_zombie(menu=None):  # always use int or string as default  - don't do as above menu=[]
    if menu is None:
        menu=[]
    menu.append('zombieee')
    return menu


if __name__=='__main__':
    print("testing the functions and arguments")

    print(add_devil())
    print (add_devil())
    print (add_devil())

    print (add_zombie())
    print (add_zombie())