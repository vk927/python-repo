
#sometimes we need to re-raise the error when we write the
def convert(s):
    '''convert to an integer'''
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print("conversion error: {}".format(str(e)))
        raise

print(convert("failx"));