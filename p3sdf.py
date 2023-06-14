"""
write a function that calculates the 
discrete convolution of two given lists.

the lists are guaranteed to have the same 
length.

reminder: the discrete convolution of two
lists a_n and b_n is another list c_n where
each element in the list is calculated by
the following formula:

           __n__
           \
    c_n =   }      a_k * a_(n-k)
           /
           -----
           k = 0

             ^
             |
 this is a notation for summation
 over k from 0 to n
"""

def convolution(list1, list2):
    pass # < fill in this function (remove the pass)

def main():
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    list1 = [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]

    conv = convolution(list1, list2)

    print(conv)

if __name__ == "__main__":
    main()
