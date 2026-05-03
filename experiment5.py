# 5. Write a menu driven program to perform the following operations on strings using string built in functions.
# a.	Find the frequency of a character in a string.
# b.	Replace a character by another character in a string.
# c.	Remove the first occurrence of a character from a string.
# d.	Remove all occurrences of a character from a string.

def remove_first_occurrence(s, char):
    return s.replace(char, '', 1)

def remove_all_occurrences(s, char):
    return s.replace(char, '')

while True:
    print("\n=== STRING OPERATIONS MENU ===")
    print("a. Find frequency of a character")
    print("b. Replace a character")
    print("c. Remove first occurrence of a character")
    print("d. Remove all occurrences of a character")
    print("0. Exit")
    
    s = input("Enter string: ")
    choice = input("Enter choice (a/b/c/d/0): ").lower()
    
    if choice == '0':
        print("Goodbye!")
        break
        
    char = input("Enter character: ")
    
    if choice == 'a':
        # Frequency using count()
        freq = s.count(char)
        print(f"Frequency of '{char}': {freq}")
        
    elif choice == 'b':
        # Replace using replace()
        new_char = input("Enter replacement character: ")
        result = s.replace(char, new_char)
        print(f"After replacement: '{result}'")
        
    elif choice == 'c':
        # Remove first occurrence using replace() with count=1
        result = remove_first_occurrence(s, char)
        print(f"After removing first '{char}': '{result}'")
        
    elif choice == 'd':
        # Remove all occurrences using replace()
        result = remove_all_occurrences(s, char)
        print(f"After removing all '{char}': '{result}'")
        
    else:
        print("Invalid choice!")

