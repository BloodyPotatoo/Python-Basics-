#Its a Date, name autofiller

name = input("Enter your name: ")
date = input("Enter the date: ")

Sentence = "Name\n You are selected for the inerview\n Date"
print(Sentence.replace("Name",name).replace("Date",date))