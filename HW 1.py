#Function to find the frequency of a digit in a number 
def main(Num, Digit):
    Num=int(Num)
    Digit=int(Digit)
    Count = 0 #Variable to store the frequency 
    while True: #Loops till the given number is reduced to 0
        if (Num % 10 == Digit): #Checks to see if the given digit appears in the given number
            Count += 1
        Num = Num // 10 #Reduces given number, eventually to 0
        if (Num == 0):
            break
    return Count
Num = input("Enter a number: ")

while Num.isdigit()==False: #Checks to see if the given input is a number
    print("Please only enter numbers")
    Num = input("Enter a number: ")
    
Digit = input("Enter a digit between 0 and 9: ")

while Digit.isdigit()==False: #Checks to see if the given input is a number
    print("Please only enter numbers")
    Digit = input("Enter a digit between 0 and 9: ")
    
while int(Digit) > 9 or int(Digit) < 0: #Cehcks to see if the given number is between 0 & 9
    print("Please enter a digit between 0 and 9")
    Digit = input("Enter a digit between 0 and 9: ")
  
print("The number of times", Digit, "appears in", Num, "is", main(Num, Digit))
#Starts the entire program and displays the output
