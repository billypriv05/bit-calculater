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


# converts decimal to binary and states how
# many bits are needed to repristent the origanl integer
def int_bits():

    # get interger (must be >= 0)
    var_integer = num_check(" please enter an interger: ", 0)

    # source for code below is
    # httpls://stackoverflow.com/questions/699866/python-int-to-binary-string

    var_binary = "{0:b} ".format(var_integer)

    # calculate the # of bits ( lenght of string above)
    num_bits = len(var_binary)

    # output answer with working\
    print()
    print("{} in binary is {}".format(var_integer, var_binary))  
    print(" # of bits {}".format(num_bits))
    print() 

    return ""

# main routine
int_bits()
      


