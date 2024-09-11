# Question 01: Simple Comparison
def is_even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(is_even_or_odd(248))

#Question 02: Age Check
def check_age_category(age):
    if age < 18:
        return "Minor"
    elif 18 <= age < 65:
        return "Adult"
    else:
        return "Senior"

print(check_age_category(10))

#Question 03:Temperature Advice
def temperature_advice(temp_celsius):
    if temp_celsius > 30:
        return "Hot"
    elif 15 <= temp_celsius <= 30:
        return "Warm"
    else:
        return "Cold"

print(temperature_advice(35))

#Question 04:Grade Evaluation
def evaluate_grade(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"

print(evaluate_grade(95)) 

#Question 05:Sum of list
def sum_list(numbers):
    return sum(numbers)

print(sum_list([21, 28, 53, 74, 235])) 

#Question 06: Print Multiples
def print_multiples(n):
    for i in range(1, 11):
        print(n * i)

print("Multiples of 5:")
print_multiples(5)


#Question 07:Reverse String
def reverse_string(s):
    return s[::-1]

print("Reversed string of 'Python':", reverse_string("Python"))

# Question 08: Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("hello world"))  

# Question 09: Countdown
def countdown(n):
    while n > 0:
        print(n)
        n -= 1
    print("Liftoff!")

countdown(5) 

# Question 10: Guess the Number
import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    guess = None
    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 100: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    print("You guessed it!")

# Question 11: Factorial Calculation
def calculate_factorial(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial

print(calculate_factorial(5))  

# Question 12: Fibonacci Sequence
def fibonacci_sequence(n):
    a, b = 0, 1
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1
    print()

fibonacci_sequence(10)  

# Question 13: Convert to Uppercase
def to_uppercase(s):
    return s.upper()

print(to_uppercase("hello world"))  

# Question 14: Calculate Square
def square_number(n):
    return n ** 2

print(square_number(24))  

# Question 15: Check Palindrome
def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("racecar"))  

# Question 16: Find Maximum
def find_maximum(numbers):
    return max(numbers)

print(find_maximum([12, 445, 273, 78, 920, 2]))  







