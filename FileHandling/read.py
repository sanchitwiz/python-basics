f = open("demo.txt", "r")

data = f.read()
data = f.readline()
# readline() prints the first line
new_data = f.readlines()
# readlines() privide list of each characters

# print(new_data[1])

"""
once a file is read, pointer went to the last, and cannot read again
"""
print(type(data))

f.close()