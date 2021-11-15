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


# finds # of bits for 24 bit colour
def image_bits():

    # get width and height
    image_width = num_check("image width? ", 1)
    image_height = num_check("image height? ", 1) 
    
    # calculate # of pixels 
    num_pixels = image_width * image_height 

    # calculate # of bits ( 24 * num of pixels)
    num_bits = num_pixels * 24

    # output the answer with working
    print()
    print("# of pixels = {} x {} = {}".format(image_height,
                                              image_width, num_pixels)
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits)
    print()
    
    return ""

# main routine goes here 
image_bits()

