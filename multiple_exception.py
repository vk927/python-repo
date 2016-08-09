import sys
def convert(s):
    '''convert to an integer'''
    try:
        return int(s)
    except (ValueError,TypeError) as e:
        print("conversion error: {}".format(str(e)),file=sys.stderr)
        return -1

print(convert("failx"));