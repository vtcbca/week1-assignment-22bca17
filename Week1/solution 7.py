#write a python script to enter any string,replace vowel with its position number.
#like Amit to 0m2t
name=input("Enter string:: ")
new_name=""
for i in range(len(name)):
    if i%2>0:
        new_name=new_name+name[i]
    else:
        new_name=new_name+str(i)
print('New Name: ',new_name)
