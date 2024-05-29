import math

# Functions

# Checks if User's Input is in given list
def list_checker(question, chosen_list, error_message):

    yes_no_list = ["yes", "no"]
    shapes_list = ["circle", "square", "triangle", "rectangle"]

    while True:
        response = input(question).lower()

        # If the response is inside the list
        if chosen_list == "yes_no":
            var_list = yes_no_list

        else:
            var_list = shapes_list

        for var_item in var_list:

            # And the response is either the word or the first 
            # letter of the word, returns the entire word
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
                    
        # Else print error message
        print(error_message)

# Checks User Input is a number
def num_check(number, error_message, exit_code):
    while True:

        # First checks if the user entered the exit code
        response = input(number).lower()
        
        if response == exit_code:
            return response

        # If not, then it checks if input was a number
        try:
            response = float(response)
    	    
            if response <= 0:
                print(error_message)
            
            else:
                return response

        except ValueError:
            print(error_message)


# Main Routine...
while True:
    print()
    # Asks user for shape chosen
    chosen_shape = list_checker("Please select a shape (Circle, Square, Triangle, or Rectangle)? ", "shapes", "Please choose from: Circle (c), Square (s), Triangle (t), or Rectangle (r)\n")

    # Depending on chosen shape, program asks different lengths
    if chosen_shape == "square":
        length = num_check("Length? " , "Please enter a number more than 0", "xxx")
    
    elif chosen_shape == "rectangle":
        length = num_check("Length? " , "Please enter a number more than 0", "xxx")
        height = num_check("Width? " , "Please enter a number more than 0", "xxx")
    
    elif chosen_shape == "triangle":
        # Asks user if they have all three sides of the triangle
        have_all_sides = list_checker("Do you have all lengths of three sides of the triangle? ", "yes_no", "Please enter either yes or no...\n")

        # If yes, asks to enter all three sides
        if have_all_sides == "yes":
            side1 = num_check("Length of Side 1? ", "Please enter a number more than 0", "xxx")
            side2 = num_check("Length of Side 2? ", "Please enter a number more than 0", "xxx")
            side3 = num_check("Length of Side 3? ", "Please enter a number more than 0", "xxx")

            # And checks that the sum of two sides is always greater than the third side
            if side1 + side2 < side3 or side3 + side2 < side1 or side3 + side1 < side2:
                print("This is an Impossible Triangle")
                continue
        
        # Else, just asks base and height
        else:
            side1 = num_check("Length of Base? ", "Please enter a number more than 0", "xxx")
            height = num_check("Height? ", "Please enter a number more than 0", "xxx")
    
    else:
        length = num_check("Radius? " , "Please enter a number more than 0", "xxx")

    # Shape Formulas
    if chosen_shape == "square":
        area = length * length
        perimeter = length * 4
    
    elif chosen_shape == "rectangle":
        area = length * height
        perimeter = (length + height) * 2
    
    elif chosen_shape == "triangle":

        if have_all_sides == "yes":
            perimeter = side1 + side2 + side3          
            area = math.sqrt((side1 + side2 + side3 / 2) * ((side1 + side2 + side3 / 2) - side1) * ((side1 + side2 + side3 / 2) - side2) * ((side1 + side2 + side3 / 2) - side3))
               
        else:
            area = side1 * height * 0.5
            perimeter = "N/A"
    
    else:
        area = math.pi * (length * length)  
        perimeter = 2 * math.pi * length

    print(f"Area: {area} , Perimeter: {perimeter}")



print("Program ends")