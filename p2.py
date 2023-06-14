"""
search through a given list and replace every 5
with an 85.

example:
    [1,2,5,7,8,15,48,5,34] -> [1,2,85,7,8,15,48,85,34]
"""

def main():
    lst = [1,5,2,5,3,5,7,6,3,7,5]
    n = len(lst) # get the number of elements in a list
    for i in range(n): # loop though the values 0...n
        pass # < fill in here (remove the pass)
    print(f"after replacing every 5 with 85: {lst}") # note: this is one of the ways to format
                                                     # strings in python (notice the f at the
                                                     # beginning and the {} surrounding lst)

if __name__ == "__main__":
    main(); # < notice that this semicolon is ignored
