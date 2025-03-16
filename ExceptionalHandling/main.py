def main():
    a = 5
    b = 2

    try:
        print("Database Connected !") 
        print(a/b)
        k = int(input("Enter a Number: "))
        print(k)
    except ZeroDivisionError as error:
        print("You cannot divide this !", error)
    except ValueError as error:
        print("Invalid Symbol Inserted !", error)
    except Exception as error:
        print("Don't know the error", error)
    finally:
        print("Database Disconnected")


    # print(a/b)

    print("Bye")

if __name__ == "__main__":
    main()