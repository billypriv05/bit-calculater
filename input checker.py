# all funtions go here
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

    
