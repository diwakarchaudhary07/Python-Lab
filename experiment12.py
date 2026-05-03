# 12. Write a program that reads a list of integers from the user and throws
#  an exception if any numbers are duplicates.
def read_unique_integers():
    try:
        # Get input from user as space-separated integers
        user_input = input("Enter a list of integers (space-separated): ")
        num_list = [int(x) for x in user_input.split()]
        
        # Check for duplicates by comparing list length with set length
        if len(num_list) != len(set(num_list)):
            raise ValueError("DuplicateError: List contains duplicate numbers!")
        
        print("All numbers are unique:", num_list)
        return num_list
        
    except ValueError as e:
        if "DuplicateError" in str(e):
            print(f"❌ {e}")
        else:
            print(f"❌ Invalid input: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# Test the program
if __name__ == "__main__":
    print("=== Test 1: Unique numbers ===")
    read_unique_integers()
    
    print("\n=== Test 2: Duplicate numbers ===")
    read_unique_integers()
    
    print("\n=== Test 3: Invalid input ===")
    read_unique_integers()
