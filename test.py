newRUL_list=[]

file = open("data.txt","r")

data = file.read()
file.close()
newRUL_list = data.split(",")
print(newRUL_list,type(newRUL_list))