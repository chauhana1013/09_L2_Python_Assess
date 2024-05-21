# Functions go here

# Checks User Input is a number
def num_check(number, error_message, exit_code):
    while True:

        # First checks if the user entered the exit code
        response = input(number).lower()
        
        if response == exit_code:
            return response

        # If not, then it checks if input was a integer
        try:
            response = int(response)
    	    
            if response <= 0:
                print(error_message)
            
            else:
                return response

        except ValueError:
            print(error_message)


# Main Routine 
while True:
    
    number_entered = num_check("Number (Enter 'xxx' to quit)? ", "Please enter a number more than 0", "xxx")
    
    # If exit code entered, Program Ends
    if number_entered == "xxx":
        break

    print(f"{number_entered}")

    

    