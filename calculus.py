import re
from sympy import symbols, integrate, diff, sympify, SympifyError
from sympy.plotting import plot


def validate_input(expression):
    """
    Validates a mathematical expression.
    Checks for allowed characters and tries to parse it using sympy.
    Returns True if valid, False otherwise.
    """
    # Define a regular expression pattern for allowed characters and basic structure
    # This includes numbers, basic arithmetic operators, parentheses, and some functions
    pattern = r'^[\d\+\-\*/\^\(\)exsincotanlogsqrt\. ]+$'

    # Check if the expression matches the pattern
    if not re.match(pattern, expression):
        print("Invalid characters in expression.")
        return False

    # Try parsing the expression using sympy
    try:
        sympify(expression)
    except SympifyError:
        print("Invalid mathematical expression.")
        return False

    # If no errors, the expression is valid
    return True

# function to get number input as int or float
def get_number_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            # Try converting to float
            value = float(user_input)
            
            # Check if it's actually an int
            if value.is_integer():
                return int(value)
            else:
                return value
        except ValueError:
            print("Please enter a valid number (int or float).")


# Plots the curve of the expression
def plot_expression(expression, lower, upper):
    # Define the symbol x
    x = symbols('x')
    # Plot the expression
    p = plot(expression, (x, lower, upper), show=False, title=f"Graph of {expression}", xlabel='x', ylabel='y')
    # Show the plot
    p.show()


# finds the area under the curve of the expression between a and b
def integrate_area(expression, a, b):
    # Define the symbol x
    x = symbols('x')
    # Compute the definite integral
    area = integrate(expression, (x, a, b))
    # Display the area
    print(f"The area under the curve from x = {a} to x = {b} is: {area}")
    
    
# derives the slope of the expression
def derive_slope(expression):
    # Define the symbol x
    x = symbols('x')
    # Compute the derivative of the expression with respect to x
    slope = diff(expression, x)
    # Display the derivative
    print(F"The derivative of the function, which represents the slope at any point x, is: {slope}")
    
    
# generates user_menu
def user_menu():
    return "(1) Plot expression\n(2) Derive area under part of the curve\n(3) Derive slope\n(q) Quit\n"
    
    
def process_choice(choice, expression):
    if choice.lower() == "q":
        exit()
    elif choice == "1":
        # define lower and upper range inputs on the y-axis to plot
        lower = get_number_input("input lower limit of range to plot:\t")
        upper = get_number_input("input upper limit of range to plot:\t")
        plot_expression(expression, lower, upper)
    elif choice == "2":
        # Define the limits of integration
        a = get_number_input("Please input lower limit for area integration:\t ")  # lower limit
        b = get_number_input("Please input upper limit for area integration:\t ")  # upper limit
        # integrate area under part of the curve
        integrate_area(expression, a, b)   
    elif choice == "3":
        # derive slope
        derive_slope(expression)
    else:
        print("invalid choice, please try again")
        
    
    
def main():
    while True:
        expression = input("please input your expression. Type q to quit:\t")
        if expression.lower() == "q":
            break
        if (validate_input(expression) == False):
            print("Invalid expression! Try again.")
        else:
            choice = input(user_menu())
            process_choice(choice, expression)
    
if __name__ == "__main__":
    main()





