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


# Rounds the number depending on if the number is whole or has decimals
def rounding(variable):
    
    while True:
        if variable % 1 == 0:
            variable = math.ceil(variable)
        else:
            variable = round(variable, 2)
        return variable

# Checks that user response is not blank
def not_blank(question):

    while True:
        response = input(question).isspace()

        # If user's response is blank, program displays this message
        if response == "" or response == False:
            print("Sorry this can't be blank. Please try again")
        
        else:
            return response


# Main Routine...
print()
yes_no_instructions = list_checker("Do want to read the instructions? ", "yes_no", "Please enter either yes or no...\n")

if yes_no_instructions == "yes": 
    print("Instructions go here...")

print()
file_name_inputed = not_blank("File Name: ")


shape_list = []
lengths_given_list = []
area_list = []
perimeter_list = []

calculations_done = 0

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
        length = rounding(length)
        shape_given = "Square"
        lengths_given = f"Length: {length}"

    elif chosen_shape == "rectangle":
        length = num_check("Length? ")
        height = num_check("Width? ")
        area = length * height
        perimeter = (length + height) * 2
        length = rounding(length)
        height = rounding(height)
        shape_given = "Rectangle"
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
            
            # Heron's Law
            else:    
                perimeter = side1 + side2 + side3  
                s = side1 + side2 + side3 / 2        
                area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                side1 = rounding(side1)
                side2 = rounding(side2)
                side3 = rounding(side3)
                shape_given = "Triangle"
                lengths_given = f"Three Sides: {side1}, {side2}, {side3}"

        # Else, just asks base and height
        else:
            side1 = num_check("Length of Base? ")
            height = num_check("Height? ")
            area = side1 * height * 0.5
            perimeter = "N/A"
            side1 = rounding(side1)
            height = rounding(height)
            shape_given = "Triangle"
            lengths_given = f"Base: {side1} Height: {height}"

    else:
        length = num_check("Radius? ")
        area = math.pi * (length * length)  
        perimeter = 2 * math.pi * length
        length = rounding(length)
        shape_given = "Circle"
        lengths_given = f"Radius: {length}"
        
    # Rounda the Area and The Perimeter
    area = rounding(area)

    if perimeter == "N/A":
        perimeter = "N/A"
        unit = ""
    
    else:
        perimeter = rounding(perimeter)
        unit = " U"

    # Outputs Area and Perimeter
    area_given = f"{area} SU"
    perimeter_given = f"{perimeter}{unit}"
    print(f"Area: {area}, Perimeter: {perimeter}")

    # Adds the following values into their respective lists
    shape_list.append(shape_given)
    lengths_given_list.append(lengths_given)
    area_list.append(area_given)
    perimeter_list.append(perimeter_given)
    
    calculations_done += 1

# Only displays the Data Frame if 1 or more calculations have been done
if calculations_done >= 1:
    question_answer_frame = pandas.DataFrame(question_answer_dict).set_index("Shape")


    # Change Dataframe to String (so it can be written to a txt file)
    question_answer_text = pandas.DataFrame.to_string(question_answer_frame)


    # Outputs the Dataframe...
    unit_text = "Rememeber: Square Units (SU) & Units (U)"

    file_name_decoration = f"***** {file_name_inputed} *****"


    to_write = [file_name_decoration, unit_text, question_answer_text]

    # Write to file...
    # Creat file to hold data (add .txt extension)
    file_name = f"{file_name_inputed}.txt"
    text_file = open(file_name, "w+")

    # Heading
    for item in to_write:
        text_file.write(item)
        text_file.write("\n\n")

    # Close File
    text_file.close()

    print()
    for items in to_write:
        print(items)
        print()

print("Program ends")