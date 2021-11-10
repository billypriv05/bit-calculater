
def num_check(question, low):
    valid = False
    while not valid:

        error = "please enter a interger that is more or than "
        "(or equal to) {}".format(low) 

        try: 

            # ask the user to enter a number        
            response = int(input(question))

            # checks if number is more than zero
            if response >= low:
                return response 

            # outputs error if imput is invalid 
            else:
                print(error)
                print() 
                
        except ValueError:
            print(error)
