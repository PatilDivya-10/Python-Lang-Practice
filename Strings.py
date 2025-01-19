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

#String Functions
str= "I am a coder."
print(str.endswith("er.")) #returns true if string ends with substr
print(str.capitalize()) #capitalize first letter
print(str.replace("a","o"))# replace substr from the str with new substr
print(str.find("am")) #return the 1st occurance if exist (no -> -1)
print(str.count("c")) #no of occurance of substr(1,2,3,etc)

