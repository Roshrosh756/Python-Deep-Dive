secret_number = 777

while True:
    user_input = int(input("Enter a three digit integer:"))

    if user_input == secret_number:
        print(f"{secret_number}")
        print("Hooray, you did it!!!")
        break
    else:
        print("Ha Ha Ha, you're stuck. Try again.")


###I learned how important it is to give correct spacing and indentation.
#  Even a single space or tab out of place causes syntax error or 
 # change the behaviour of program.
 



