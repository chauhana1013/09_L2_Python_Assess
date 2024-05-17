# Checks if User's Input was either a Yes or No
# If User inputs something else, it displays error message
def select_shape(question):

    shapes_list =  ["circle", "square", "triangle", "rectangle"]

    while True:

        response = input(question).lower()

        # If the response is inside the list
        for var_item in shapes_list:
            # And the response is either the word or the first 
            # letter of the word, returns the entire word
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
            
        print("Please choose from: Circle (c), Square (s), Triangle (t), or Rectangle (r)\n")

# Main Routine...
        
# Loop for testing
while True: 
    chosen_shape = select_shape("Please select a shape (Circle, Square, Triangle, or Rectangle)? ")
    
    print(f"You chose {chosen_shape}")