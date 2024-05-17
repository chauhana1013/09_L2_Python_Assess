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

# Main Routine...
        
# Loop for testing
yes_no_instructions = list_checker("Do want to read the instructions? ", "yes_no", "Please enter either yes or no...\n")

if yes_no_instructions == "yes": 
    print("Instructions go here...")

else:
    print("Program Continues")

print()
chosen_shape = list_checker("Please select a shape (Circle, Square, Triangle, or Rectangle)? ", "shapes", "Please choose from: Circle (c), Square (s), Triangle (t), or Rectangle (r)\n")

print(f"You chose {chosen_shape}")