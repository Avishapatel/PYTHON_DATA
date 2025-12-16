# Basic Python For Loop Tasks

#  Print numbers from 1 to 50.
#  Print the multiplication table of a number entered by the user.
#  Find the sum of numbers from 1 to 100.
#  Print each character of a given string.
#  Find the factorial of a number entered by the user.


# if..else:

# Write a program to check whether a given character is a vowel, consonant, digit, or special character.
# Take marks of 5 subjects from the user, calculate the percentage and print the grade using if..else (A, B, C, Fail).
# Take an integer input and check whether it is even or odd, and if even, also check if it is divisible by 4.

# A shop gives discounts: If the bill is more than 5000 → 20% discount, if between 2000–5000 → 10% discount, else no discount. Calculate the final price.

# Find the second largest among three numbers using only if..else.
# Classify a character entered by the user as uppercase, lowercase, digit, or special symbol.



j=True
while j:
    n=int(input("Enter year = "))
    if n%4==0 and n%100!=0 or n%400==0:
        print(n,"leap year")
    else:
        print(n,"not leap year")
    choice=input("enter yes or no ").strip().lower()
    if choice=="yes":
        j=True
    else:
        j=False