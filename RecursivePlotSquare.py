import matplotlib.pyplot as plt
def square(x,y,size,temp):
    '''
    Objective: To plot a square
    Input Parameters: x, y - lists of x coordinates and y
                      coordinates respectively
                      temp- temprorly store axis of square
    Return Value: a square 
    '''
    #Approach- Recursive
    if(size>0):
        
        x = [temp, size, size, temp, temp]
        y = [temp, temp, size, size, temp]
        plt.plot(x, y, 'ro--')
        return square(x,y,size-1,temp+1)
def main():
    '''
    Objective: To plot a square based on user input
    Input Parameter: x, y - lists of x coordinates and y
    coordinates respectively
    Return Value: None
    '''
    #Approach- Call Function square()
    size = int(input('Enter size of the square: '))
    x = [0, size, size,0,0]
    y = [0,0, size, size,0]
    temp=-1
    square(x, y,size,temp)
    plt.title('Square')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.grid()
    plt.show()
if __name__ == '__main__':
    main()
