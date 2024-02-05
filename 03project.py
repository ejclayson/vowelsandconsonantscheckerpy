import sys

def my_function():
    userInput = input("Please enter a string of pure characters with no spaces:\nType \"exit\" to end the program:\n")
    my_function2(userInput);    

def my_function2(userInput):
    while userInput != "exit":
        userInputNoSpaces = userInput.replace(" ", "")
        pattern = "[0-9.]+";
        if len(userInputNoSpaces) != 0:
            if userInputNoSpaces != pattern:
                if not userInputNoSpaces.__contains__("\\s") and not userInputNoSpaces.__contains__("\t"):
                    for x in range(len(userInputNoSpaces)):
                            if userInputNoSpaces[x].lower() == "a" or userInputNoSpaces[x].lower() == "e" or userInputNoSpaces[x].lower() == "i" or userInputNoSpaces[x].lower() == "o" or userInputNoSpaces[x].lower() == "u":
                                print(userInputNoSpaces[x] + " is a vowel.")
                            else:
                                print(userInputNoSpaces[x] + " is a consonant.")
                    my_function();
                else:
                    print("The string you supplied contains not purely characters. Thanks.")
                    my_function();
            else:
                print("You have not entered a string with pure characters")
                my_function();
        else:
            print("You have entered an empty string")
            my_function();
    else:
        my_function3();


def my_function3():
    sys.exit()

my_function();

