#Its a Book store system
Books = []
input_1 = input("Enter the name of the book: ")
Books.append(input_1)
input_2 = input("Enter the name of the book: ")
Books.append(input_1)
input_3 = input("Enter the name of the book: ")
Books.append(input_1)
input_4 = input("Enter the name of the book: ")
Books.append(input_1)
input_5 = input("Enter the name of the book: ")
Books.append(input_1)
print(Books)

if("Goku" in Books):
    print("Goku is also present in the list, GOOD!")
else:
    print("Goku is not present in the list, you should add it!")
    input_6 = input("Enter the name of Goku: ")
    Books.append(input_6)
print(Books)