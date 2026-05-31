# practice_10_exercises.py
"""
Practice Exercises with Solutions
"""

# Exercise 1: Reverse a string without using [::-1]
print("=== Exercise 1: Reverse String ===")
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

print(f"Reverse of 'Python': {reverse_string('Python')}")

# Exercise 2: Find the most frequent element in a list
print("\n=== Exercise 2: Most Frequent Element ===")
def most_frequent(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return max(frequency, key=frequency.get)

numbers = [1, 3, 2, 3, 4, 3, 5, 3, 2]
print(f"Most frequent in {numbers}: {most_frequent(numbers)}")

# Exercise 3: Check if two strings are anagrams
print("\n=== Exercise 3: Anagram Checker ===")
def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

print(f"'listen' and 'silent': {are_anagrams('listen', 'silent')}")
print(f"'hello' and 'world': {are_anagrams('hello', 'world')}")

# Exercise 4: Remove duplicates from a list
print("\n=== Exercise 4: Remove Duplicates ===")
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

duplicates = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(f"Original: {duplicates}")
print(f"Without duplicates: {remove_duplicates(duplicates)}")

# Exercise 5: FizzBuzz
print("\n=== Exercise 5: FizzBuzz ===")
def fizzbuzz(n):
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
    print()

fizzbuzz(20)