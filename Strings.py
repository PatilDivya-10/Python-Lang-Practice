#ways to store string in var
str1= "This is string"
str2='single quote'
str3="""This is string"""
#Operations -Concatenation (+ operator)
print(str1+str2)
#length() operation 
print(len(str3))
#access ch with index no but can't modify
ch=str1[3]
print(ch)
#slicing in string
st = "Divya Patil"
print(st[0:4])
print(st[1:6])
print(st[5:len(st)])
print(st[3:])#last index
print(st[:5])#start from 0
#slicing negative (reverse)
s="Apple"
print(s[-3:-1]) #pl <- op

