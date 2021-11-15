# funtions go here

# puts a series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # make string with five characters
    end = decoration * 5

    # add decoration to the start and end of the statement
    statement = "{} {} {}".format(end, text, end,)

    print()   
    print(statement)
    print()

    return ""


def user_choice():

    #list of valid responces 
    Text_ok = ["text","t", "txt"]
    interger_ok = ["integer", "int", "#", "number"]
    image_ok = ["image", "img", "pix", "picture", "pic"]

    valid = False
    while not valid:

       # ask for user for choice and change responce for lower case
       response = input("file type (integer/ text/ image): ").lower()

       # checks for vaild response and returns text, interger or image

       if response in Text_ok:
           return "text"

       elif response in interger_ok:
           return "integer"

       elif response in image_ok:
           return "integer"
       elif response == "i":
           want_interger = input("press <enter> for an interger or any key for an image")
           if want_interger == "":
               return "interger"
           else:
               return "image"
       else: 
           # if response is not valid, output an error 
           print("please choose a valid file type!")
           print()    

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

# calculates the # of bits for text (# of characters x 8)
def text_bits(): 

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
    print("# of pixels = {} x {} = {}".format(image_height, image_width, num_pixels))
    print("# of bits = {} x 24 = {}".format(num_pixels, num_bits))
    print()
    
    return ""

# main routene goes here

# heading
 statement_generator("bit calculater for, text & images","-")


# display instruction if user has not used the program before

# loop to allow multiple calculation per session. 
keep_going = ""
while keep_going == "": 

    # ask the user for the file type 
    data_type = user_choice()
    print("you chose", data_type)

    # for intergers, ask for interger 
    if data_type =="interger":
        int_bits()
    # for images, ask for witdh and height 
    # (must be an interger more than / eqaul to 1)
    elif data_type == "image":
         image_bits() 
    
    # for text, ask for a string   
    else:
        text_bits()

    print() 
    keep_going = input("press <enter> to continue or any other key to quit")
    print()

    
    





    



                  
