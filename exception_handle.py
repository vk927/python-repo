def convert(s):
    '''convert to an integer'''
    try:
        x=int(s)
        print("conversion succeeded! x=",x)
    except ValueError:
        print("onversion failed")
        x=-1
    return x

print (convert("bchsg"))