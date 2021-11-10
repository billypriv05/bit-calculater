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

# main routene goes here
statement_generator("look-stars", "*")
