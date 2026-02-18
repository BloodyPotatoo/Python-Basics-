#Its a small dictionary program
words = {
    "What": "क्या",
    "Where": "कहाँ",
    "When": "कब",
    "Why": "क्यों",
}

user_input_1 = input("Enter the word you want to translate: ")
if user_input_1 in words:
    print(words.get(user_input_1))
    print(f"The meaning of {user_input_1} is {words.get(user_input_1)}")
elif user_input_1 not in words:
    print("Sorry its not in your dictionary, But you cna add it!")
    user_input_2 = input("Enter the meaning of the word: ")
    words.update({user_input_1: user_input_2})
    print(words.get(user_input_1))

else: 
    user_input_1 == ""
    print("Please enter a word to translate")