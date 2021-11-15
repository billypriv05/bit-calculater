# calculates the # of bits for text (# of characters x 8)
def text_bits():

    print()
    # ask user for string...
    var_text = input("enter some text: ")

    # calculate # of bits (length of string x 8)
    var_length = len(var_text)
    num_bits = 8 * var_length

    # outputs answer with working
    print()
    print("/'{}/' has {} characters ...".format(var_text, var_length))  
    print("# of bits is {} x 8...".format(num_bits, var_text))
    print()

    return ""
# main routine goes here
text_bits()             
