list=['hi',1,2]
print(list[0])
list[0]=2
print(list[0])
print(list)

tuple=('hiiiii',1,2)
print(tuple[0])
print (len(tuple))
#tuple[0]=2   # we get error because tuple object does not support item assignment as list
print(tuple[0])
print(tuple)


for item in tuple:
    print('+++++++++++',item)

#single element tuple
#t=(1) -- error
t=(1,)
print (t[0],"------------")