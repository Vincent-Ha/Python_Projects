def downward_box(number):
    ''' Function creates a series of downward boxes that run diagonally down
        to the right. The number of boxes created is based on the number given
        to the function.'''
    print('+-+') #prints the first line of the boxes
    
    for index in range(number): # prints the rest of the boxes based on the input
                                # given
        print((index * 2) * ' ' + '| |') # prints the sides of the box
        print((index * 2) * ' ' + '+-+-+' if (index < number - 1) else (index * 2) * ' ' + '+-+')
                # Prints the tops and bottoms of the boxes. Would print '+-+-+'
                # unless it is the last line, in which case would print '+-+'
         
# Main Function
number = int(input())
downward_box(number)
