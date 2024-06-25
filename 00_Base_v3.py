# Imports up here...
import math
import pandas

# Functions go here... 

# Checks if User's Input is in given list
def list_checker(question, chosen_list, error_message):

    yes_no_list = ["yes", "no"]
    shapes_list = ["circle", "square", "triangle", "rectangle", "xxx"]

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
def num_check(number):
    while True:
        # If not, then it checks if input was a number
        try:
            var_response = float(input(number))
    	    
            if var_response <= 0:
                print("Please enter a number more than 0")
            
            else:
                return var_response

        except ValueError:
            print("Please enter a number more than 0")

# Main Routine...
print()
yes_no_instructions = list_checker("Do want to read the instructions? ", "yes_no", "Please enter either yes or no...\n")

if yes_no_instructions == "yes": 
    print("Instructions go here...")

shape_list = []
lengths_given_list = []
area_list = []
perimeter_list = []


# Main Routine...
while True:

    question_answer_dict = {
    "Shape": shape_list,
    "Length": lengths_given_list,
    "Area": area_list,
    "Perimeter": perimeter_list
    }

    print()
    # Asks user for shape chosen
    chosen_shape = list_checker("Please select a shape (Circle, Square, Triangle, Rectangle or 'xxx' to quit)? ", "shapes", "Please choose from: Circle (c), Square (s), Triangle (t), Rectangle (r) or 'xxx' to quit\n")

    if chosen_shape == "xxx":
        break

    # Depending on chosen shape, program asks different lengths
    if chosen_shape == "square":
        length = num_check("Length? ")
        area = length * length
        perimeter = length * 4
        lengths_given = f"Length: {length}"

    elif chosen_shape == "rectangle":
        length = num_check("Length? ")
        height = num_check("Width? ")
        area = length * height
        perimeter = (length + height) * 2
        lengths_given = f"Length: {length} Width: {height}"

    
    elif chosen_shape == "triangle":
        # Asks user if they have all three sides of the triangle
        have_all_sides = list_checker("Do you have all lengths of three sides of the triangle? ", "yes_no", "Please enter either yes or no...\n")

        # If yes, asks to enter all three sides
        if have_all_sides == "yes":
            side1 = num_check("Length of Side 1? ")
            side2 = num_check("Length of Side 2? ")
            side3 = num_check("Length of Side 3? ")

            # And checks that the sum of two sides is always greater than the third side
            if side1 + side2 < side3 or side3 + side2 < side1 or side3 + side1 < side2:
                print("This is an Impossible Triangle")
                continue
            
            else:    
                perimeter = side1 + side2 + side3  
                s = side1 + side2 + side3 / 2        
                area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                lengths_given = f"Three Sides: {side1}, {side2}, {side3}"

        # Else, just asks base and height
        else:
            side1 = num_check("Length of Base? ")
            height = num_check("Height? ")
            area = side1 * height * 0.5
            perimeter = "N/A"
            lengths_given = f"Base: {side1} Height: {height}"


    else:
        length = num_check("Radius? ")
        area = math.pi * (length * length)  
        perimeter = 2 * math.pi * length
        lengths_given = f"Radius: {length}"
    
    
    # Checks if area and perimeter are whole numbers or numbers with decimals
    # And rounds accordingly
    if area % 1 == 0:
        area = math.ceil(area)
    else:
        area = round(area, 2)
    
    if perimeter == "N/A":
        perimeter = "N/A"

    elif perimeter % 1 == 0:
        perimeter = math.ceil(perimeter)
    else:
        perimeter = round(perimeter, 2)

    # Outputs Area and Perimeter
    print(f"Area: {area}, Perimeter: {perimeter}")

    # Adds the following values into their respective lists
    # But there are couple issues
    shape_list.append(chosen_shape)
    lengths_given_list.append(lengths_given)
    area_list.append(area)
    perimeter_list.append(perimeter)

question_answer_frame = pandas.DataFrame(question_answer_dict)


# Change Dataframe to String (so it can be written to a txt file)
question_answer_text = pandas.DataFrame.to_string(question_answer_frame)

# Outputs the Dataframe...
file_name_inputed = "Pandas Formating Testing #1"
to_write = [file_name_inputed, question_answer_text]

for items in to_write:
    print(items)
    print()

print("Program ends")