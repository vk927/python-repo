count=0
def show_count():
    print("The initial count is ...")
    print("count=",count)


def set_count(c):

    print ("setting the count to" , c)
    count=c # c assigned only locally not globally  ----- local binding of count
    print("count=", count)

# use global to assign to global references from a local scope

def set_global_count(c):
    print ("setting the count to" , c)
    global count  # calling a global variable inside a definition
    count=c  # now globally binding
    print("count=", count)

show_count()
set_count(5) # assigning 5 locally
show_count()  # we get again 0 not 5 because 5 is
set_global_count(51) # we are assigning it globally
show_count()