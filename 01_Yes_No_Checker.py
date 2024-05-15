# Checks if User's Input was either a Yes or No
# If User inputs something else, it displays error message
def yes_no(question):

    to_check = ["yes", "no"]

    while True:

        response = input(question).lower()

        # If the response is inside the list
        for var_item in to_check:
            # And the response is either the word or the first 
            # letter of the word, returns the entire word
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item
        print("Please enter either yes or no...\n")

# Main Routine...
        
# Loop for testing
while True: 
    yes_no_instructions = yes_no("Do want to read the instructions? ")
    
    if yes_no_instructions == "yes": 
        print("Instructions go here...")
    
    else:
        print("Program Continues")