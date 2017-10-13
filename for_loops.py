# This handles the thread to allow the loop to pause slightly
from time import sleep


""" Firstly, I just wanted to talk a little bit about For loops
 
    Python For loops are a little different to other for loops in other languages
    such as a C#, Java, and C++ (all have the same for loop syntax)
    
    for loop; for example:
    
            for(int i = 0; i < 12; i++) { do something } <-- C#
            
    Python For loops are more like C# Foreach loops; however work in the same way
    as a normal for loop (I will give you multiple examples of what I mean)
    
        for i in myList: <-- Python for loop
        
        foreach(int item in myList) { do something } <-- C# example
        
    Foreach loops are looping mechanisms that iterate through individual items; 
    you would normally use a foreach loop in C# to loop through the contents of a
    List or an array
    
    """

#####################################################################
#
#
#       SECTION 1: For Loops
#
#
######################################################################


# First for loop we will write is a simple loop to print out the numbers 1-10
# The ':' is really important to include, it lets the python interpreter know we are writing a for loop
for num in range(11):
    print(num)
    sleep(1)  # This just tells the loop to wait 1 seconds before printing the next number


print('\n' * 3)  # A short hand way of writing multiple newlines


# The next loop we can loop through a list an print out the items
# First we need to define the list we want to loop through
premier_League_clubs = ['Swansea City', 'Manchester United', 'Chelsea', 'Liverpool', 'Arsenal',
                            'West Ham', 'West Brom']

for team in premier_League_clubs:
    print(team, sep=" ")  # The ',' print the items on one line



print('\n' * 3)

# We can also break out of loops with the 'break' keyword
for num in range(4):
    # we can write an if statement to break when the loop hits the 2nd number
    if num == 2:
        print('The iterator number is: %d' % num)
        break



""" We can also use nested loops, which are loops inside of loops
  
    The tricky thing to understand about nested loops is variable scope
    
    I will add comments within the nested loops to explain this
    
    When I mention variable scope, I actually mean whether or not the variable can
    be accessed
"""

print('\n' * 3)

for xNum in range(1, 11):

    # xNum's scope

    for yNum in range(1, 11):

        # xNum can be accessed here because the 2nd for loop is within the scope of xNum's for loop

        print('%d * %d = %d' % (xNum, yNum, xNum * yNum))

    print('\n')


print('\n' * 3)


# I will show you how to write the bubble sort algorithm using a for loop
# Because we will use the same alogrithm on multiple lists we should put it
# into a function (I normally call these 'methods' but thats because I'm used to C type languages)
# To write a function we need to define it, name it, and then provide the parameters that it will take in
# Such as:
def bubbleSortAlgorithm(unsortedList):

    # This line means loop through the list passed into the function
    # and start at index[0] and return -1 if there is an error
    for passnum in range(len(unsortedList)-1, 0, -1):

        # This loop looks to sort each item within the list we pass into the function
        for item in range(passnum):

            if unsortedList[item] > unsortedList[item + 1]:

                # The next three lines handle the swapping mechanism of each set of
                # 2 pairs of numbers from the unsortedList
                temp = unsortedList[item]
                unsortedList[item] = unsortedList[item + 1]
                unsortedList[item + 1] = temp



# Now, we can define a few unordered lists and pass them into the function and print the result

unorderedList1 = [20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]

print('UnorderedList1:', unorderedList1)  # ',' is a shorthand way of adding a space
bubbleSortAlgorithm(unorderedList1)
print('Ordered List:', unorderedList1)

unorderedList2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print('UnorderList2:', unorderedList2)
bubbleSortAlgorithm(unorderedList2)
print('Ordered List2:', unorderedList2)


""" I hope this has helped to understand a bit more about what for loops do
    One way to fully understand is to try and (re)implement the same or different for loops
    
    One note on the Bubble Sort: although it is classed as the most inefficient sorting method there
    is another way to write the sorting method so that it stops when it finds out that the list is sorted.
    This can be known as the short bubble sort. I will show you how that is implemented when I send over a 
    file about while loops
    
 """















