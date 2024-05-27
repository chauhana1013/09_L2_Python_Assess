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
            return "xxx"

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
while != "xxx":
    print()
    chosen_shape = list_checker("Please select a shape (Circle, Square, Triangle, or Rectangle)? ", "shapes", "Please choose from: Circle (c), Square (s), Triangle (t), or Rectangle (r)\n")

    if chosen_shape == "square":
        length = num_check("Length? " , "Please enter a number more than 0", "xxx")
    
    elif chosen_shape == "rectangle":
        length = num_check("Length? " , "Please enter a number more than 0", "xxx")
        width = num_check("Width? " , "Please enter a number more than 0", "xxx")
    
    elif chosen_shape == "triangle":
        have_all_sides = list_checker("Do you have all three sides of the triangle? ", "yes_no", "Please enter either yes or no...\n")

        if have_all_sides == "yes":
            side1 = num_check("Length of Side 1? ", "Please enter a number more than 0", "xxx")
            side2 = num_check("Length of Side 1? ", "Please enter a number more than 0", "xxx")
            side3 = num_check("Length of Side 1? ", "Please enter a number more than 0", "xxx")

            if side1 + side2 < side3 or side3 + side2 < side1 or side3 + side1 < side2:
                print("This is an Impossible Triangle")
                continue
            
        else:
            side1 = num_check("Length of Base? ", "Please enter a number more than 0", "xxx")
            height = num_check("Height? ", "Please enter a number more than 0", "xxx")
    


print("Program ends")