with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java\nI like programming in Java")


with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")
    print(new_data)


with open("practice.txt", "w") as f:
    f.write(new_data)


with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning")):
        print(True)
    else:
        print(False)


def check_for_word():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1

if __name__ == "__main__":
    check_for_word()