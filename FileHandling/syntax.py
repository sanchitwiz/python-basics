with open("sample.txt", "r") as f:
    data = f.read()
    print(data)


with open("sample.txt", "w") as f:
    f.write("Sanchit is a Good boy")