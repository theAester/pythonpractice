"""
write a for loop that prodces
the shape below:


    *
    * *
    * * *
    * * * *
    * * * * *
    ... (n times)

where n is read from the input
"""

"""
this example is completed for you to learn 
bout basic for loop and printing. you dont 
need to write any code. just read the 
given code and analyse it.
"""

def main():
    n = int(input()) # this is how we read an integer from input. 
                     # the input() function reads a line from the
                     # input. the output is always a string.
                     # the int() function tries to convert the 
                     # string into an integer

    for i in range(n): # loop through values 0...n, including 0 and not including n
        line = "" # define an empty string
        for j in range(i): # loop through values 0...i, including 0 and not including i
            line += "* " # concatenation is done using the + operator between strings
        print (line)

if __name__ == "__main__":
    main()
