# funtions go here

# puts a series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration):

    # make string with five characters
    end = decoration * 5

    # add decoration to the start and end of the statement
    statement = "{} {} {}".format(ends, text, ends,)

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
    # (must be an interger more than / eqaul to 0)

    # for images, ask for witdh and height 



                  
