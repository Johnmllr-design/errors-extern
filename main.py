# a file for the error handling portion fo the externship

i = None
try:
    i = int(input("give me an number: "))
    result = 100 / i
except ZeroDivisionError:
    print("Oops! You cannot divide by zero.")
except ValueError:
    print("Invalid input! Please enter a valid number.")
else:
    print("result is " + str(result))



# indexError
try:
    my_list = [10, 20, 30]
    # Trying to access index 5 (which doesn't exist) will raise IndexError
    print(my_list[5])
except IndexError:
    print("IndexError: That index does not exist in the list.")

# KeyError 
try:
    my_dict = {"name": "John", "age": 21}
    # Accessing a key that doesn't exist in the dictionary
    print(my_dict["height"])
except KeyError:
    print("KeyError: That key does not exist in the dictionary.")


# TypeError 
try:
    # Attempting to add a string and an integer raises TypeError
    result = "Age: " + 21 # type: ignore
    print(result)
except TypeError:
    print("TypeError: You cannot add a string and an integer.")


# part three: try except else finally

try:
    # Prompt the user to enter two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Try to perform division
    result = num1 / num2

except ZeroDivisionError:
    # Handle division by zero
    print("Error: Cannot divide by zero.")

except ValueError:
    # Handle non-numeric input
    print("Error: Please enter valid numbers.")

else:
    # Only runs if no exceptions occur
    print(f"{num1} divided by {num2} is {result}.")

finally:
    # Runs no matter what
    print("Thank you for using the division program.")