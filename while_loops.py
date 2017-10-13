
""" While loops are quite similar to For loops in that they operate depending on a condition """



################################################################################################
#
#
#                               Section 2: While Loops
#
#
#
################################################################################################


# The first important loop I want to mention is:

    #while True:
        # Do Something

# Never write a loop like the one above as it will never stop and could burn your processor out
# Only write this type of while loop if you allow the loop to escape (Example below)
# As mentioned about you need to give a while loop a condition to adhere to

# For example

"""i = 0
while i < 11:

    print(i)
    i += 1


print('\n' * 3)
"""

# We can use a while loop to check whether a user enters a valid number that we deem valid
# For this example we only want to accept numbers between 10 and 20
"""invalidNumber = True
while invalidNumber:

    number = int(input('Please enter a number between 10 and 20: '))
    if number >= 10 and number <= 20:
        invalidNumber = False
    else:
        print('\nSorry, the number must between 10 and 20')
        print('Please try again')


print('\nYou entered {0}'.format(number))
print('This is a valid number')
"""



# Another example
# We can also use a while loop to test for a users correct password
# Let's say for this example the password is 'secret'

"""password = ""
while password != 'secret':
    password = input('Enter your password: ')

    if password == 'secret':
        print('\nYou have entered the correct password')

    else:
        print('\nPlease try again')

"""

# Now, that we have knowledge on while loops I can show you how to write the short bubble sort algorithm
# We def a function in the same way as before
def shortBubbleAlgorithm(unsortedlist):

    exchanges = True
    passnum = len(unsortedlist) - 1

    while passnum > 0 and exchanges:
        exchanges = False

        for i in range(passnum):
            if unsortedlist[i] > unsortedlist[i + 1]:
                exchanges = True
                temp = unsortedlist[i]
                unsortedlist[i] = unsortedlist[i + 1]
                unsortedlist[i + 1] = temp

        passnum = passnum - 1



unorderedList=[20,30,40,90,50,60,70,80,100,110]
print('UnorderedList:', unorderedList)

shortBubbleAlgorithm(unorderedList)

print('SortedList:', unorderedList)





















