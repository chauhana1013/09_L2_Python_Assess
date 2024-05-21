# Functions go here
def num_check(number, error_message, exit_code):
    while True:
        response = input(number).lower()
        
        if response == exit_code:
            return response

        try:
            response = float(response)
    	    
            if response <= 0:
                print(error_message)
            
            else:
                return response

        except ValueError:
            print(error_message)


# Main Routine 
while True:
    
    number_entered = num_check("Number (Enter 'xxx' to quit)? ", "Please enter a number more than 0", "xxx")
    
    if number_entered == "xxx":
        break

    print(f"{number_entered}")

    

    