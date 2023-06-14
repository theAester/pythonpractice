"""
search through a given list and replace every 5
DIGIT with an 85.

this part is different from part2 (p2.py)
to understand check out the example.

example:
    input:
    [1,2,5,7,8,15,48,5,34]

    output:
    [1,2,85,7,8,185,48,85,34]

notice how this time the 15 in the input
list also turned into a 185
"""

# can you explain what the pre-existing code does?
def replace_all_5s(num): # note: this is how we define functions
    newnum = 0
    while num != 0:
        digit = num%10
        num /= 10
        # < fill in here
    return newnum

def main():
    lst = [1,5,2,51,35,5,75,6,503,575,5]
    for i in range(len(lst)): 
        lst[i] = replace_all_5s(lst[i])
    print(lst)


if __name__ == "__main__":
    main(); 
