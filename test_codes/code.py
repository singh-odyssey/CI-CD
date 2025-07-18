import math
import random
import datetime

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def factorial(n):
    if n < 0:
        return None
    return math.factorial(n)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def random_list(size, lower=0, upper=100):
    return [random.randint(lower, upper) for _ in range(size)]

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def get_current_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def fibonacci(n):
    if n <= 0:
        return []
    seq = [0, 1]
    while len(seq) < n:
        seq.append(seq[-1] + seq[-2])
    return seq[:n]

def unique_elements(lst):
    return list(set(lst))

def sort_list(lst):
    return sorted(lst)

def word_count(s):
    return len(s.split())

def is_palindrome(s):
    return s == s[::-1]

def sum_list(lst):
    return sum(lst)

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def main():
    print("Add:", add(5, 3))
    print("Subtract:", subtract(10, 4))
    print("Multiply:", multiply(6, 7))
    print("Divide:", divide(8, 2))
    print("Factorial:", factorial(5))
    print("Is Prime:", is_prime(17))
    print("Random List:", random_list(5))
    print("Reverse String:", reverse_string("hello"))
    print("Count Vowels:", count_vowels("Programming"))
    print("Current Datetime:", get_current_datetime())
    print("Fibonacci:", fibonacci(7))
    print("Unique Elements:", unique_elements([1, 2, 2, 3, 4, 4, 5]))
    print("Sorted List:", sort_list([5, 2, 9, 1]))
    print("Word Count:", word_count("Hello world from Python"))

    # User input based demonstration
    user_str = input("Enter a string to check palindrome: ")
    print(f"Is Palindrome: {is_palindrome(user_str)}")

    user_list = input("Enter numbers separated by space to sum: ")
    num_list = [int(x) for x in user_list.split()]
    print(f"Sum of List: {sum_list(num_list)}")

    celsius = float(input("Enter Celsius temperature to convert: "))
    print(f"Fahrenheit: {celsius_to_fahrenheit(celsius)}")

if __name__ == "__main__":
    main()