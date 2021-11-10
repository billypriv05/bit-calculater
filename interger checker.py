# checks imput is a number more than 
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

# main routine goes here 

keep_going = ""
while keep_going == "":
    print()
    # ask user for an interger (must be than / equal to 0)
    var_interger = num_check("enter an interger: ", 0)
    print()

    # ask for width and height of an image 
    # (must be more than / equal to 1 )
    image_width = num_check("image width?", 1)
    print()
    image_height = num_check("image height?", 1)
