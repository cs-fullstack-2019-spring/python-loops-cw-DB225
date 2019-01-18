def main():
#EXERCISE1
#Print -20 to and including 50.
# Use any loop you want.
    for num in range(-20, 51):
        print(num)
###########################################################################################################
#EXERCISE2
#Create a loop that prints even numbers from 0 to and including 20.
    for num in range(21):
        print(num)
###########################################################################################################
#EXERCISE3
#Prompt the user for 3 numbers.
# Then print the 3 numbers along with their average after the 3rd number is entered.
# Refer to example below replacing NUMBER1, NUMBER2, NUMBER3, and THEAVERAGE with the actual values.
    userInput1 = int(input("Write the first number: "))
    userInput2 = int(input("Write the second number: "))
    userInput3 = int(input("Write the third number: "))
    total = (userInput1+userInput2+userInput3)/3
    print("The average of "+str(userInput1)+", "+str(userInput2)+" and "+str(userInput3)+" is "+str(total))
###################################################################################################################
#EXERCISE4
#Password Checker - Ask the user to enter a password. Ask them to confirm the password.
# If it's not equal, keep asking until it's correct or they enter 'Q' to quit.
    userInput = input("Enter the password: ")
    userConfirm = input("Confirm the password: ")
    password = "ABCD"

    while(userInput != "Q" or userConfirm != "Q"):
        if(userInput == password and userConfirm == password):
            print("CORRECT")
        elif(userInput != password or userConfirm != password):
            print(" ")
        break
######################################################################################################################
#BONUS:
#FIZZBUZZ is the classic Programmer's challenge often used as part of job interviews:
#Prompt the User for the ending value (e.g. 100)
#Your code should start at 1 and then iterate each number up to the ending value entered by the user
#If the current number is evenly divisible by 3 you should print FIZZ and the number
#If the current number is evenly divisible by 5 you should print BUZZ and the number
#If the current number is evenly divisible by both 3 and 5 you should print FIZZBUZZ and the number to the screen
#Otherwise, just print the original number
    userInput = int(input("Input a value: "))
    for eachEl in range(1,(userInput-1)):
        if eachEl%15 == 0:
            print("FIZZBUZZ")
        elif eachEl%3 == 0:
            print("FIZZ")
        elif eachEl%5 == 0:
            print("BUZZ")
        else:
            print(eachEl)






####################################################################################################################
if __name__ == '__main__':
    main()