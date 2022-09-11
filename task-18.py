names=['mahmoud','farida','ali','hassan','mohamed','khaled','taha']

print('''--------------------------------
names to uppercase -[normal list\n''')
new_names1=[]
for i in names:
    new_names1.append(i.upper())
print(new_names1)


print('''--------------------------------
names to uppercase - list comprehension\n''')

new_names2=[n.upper() for n in names]
print(new_names2)


print('''--------------------------------
names to uppercase - functional programming\n''')
def uppercase(names):
    return names.upper()

new_names3=map(uppercase,names)
print(list(new_names3))

print('''--------------------------------
names that contains ‘a’ - normal list\n''')

new_names4=[]
for i in names:
    if 'a' in i:
        new_names4.append(i)
print(new_names4)


print('''--------------------------------
names that contains ‘a’ - list comprehension\n''')
new_names4=[i for i in names if 'a' in i ]
print(new_names4)

print('''--------------------------------
names that contains ‘a’ - functional programming\n''')

def a_ther(name):
    if 'a' in name:
        return name
new_names5=map(a_ther,names)
print(list(new_names5))

print('''--------------------------------
 names that starts with ‘t’ - normal list\n''')
new_names6=[]
for n in names:
    if n[:1]=='t':
        new_names6.append(n)
print(new_names6)



print('''--------------------------------
 names that starts with ‘t’ - functional programming\n''')
d=[]
def liststartwith_t(n):
    if n[:1]=='t':
        return n
new_names7=map(liststartwith_t,names)
print(list(new_names7))

print('''--------------------------------
 names that starts with ‘t’ - list comprehension\n''')

new_names8=[i for i in names if i[:1]=='t']
print(list(new_names8))


print('''--------------------------------
 names that contains 2 or more ‘a’ - normal list\n''')

new_names9=[]
for i in names:
    count=i.count('a')
    if count>=2:
        new_names9.append(i)

print(new_names9)


print('''--------------------------------
 names that contains 2 or more ‘a’ - functional programming\n''')

def count_a(n):
    p=n.count('a')
    if p >=2:
        return n
new_names9=map(count_a,names)
print(list(new_names9))



print('''--------------------------------
 names that contains 2 or more ‘a’ - list comprehension\n''')

new_names10=[i for i in names if i.count('a')>=2]
print(list(new_names10))


print('''--------------------------------
  a= the first index , b = rest of the list\n''')
print(names)

a,*b=names
print(a)
print(b)


print('''--------------------------------
  a = the first index , b = the last index\n''')
print(names)
a,*_,b=names
print(a)
print(b)


print('''--------------------------------
  a = the first index , b = the second index\n''')
print(names)
a,b,*_=names
print(a)
print(b)
