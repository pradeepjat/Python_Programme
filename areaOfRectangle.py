def areaOfRectangle(length,breadth):
    '''
    Objective: To print a area of rectangle using input
    Input Parrameter: 
             length->length of rectangle
             breadth->breadth of rectangle
    Result : Area of rectangle
    '''
    #Approach : area=length * breadth
    area = length*breadth
    return area

def main():
    '''
    Objective: To print a area of rectangle using input
    Input Parrameter:
             length->length of rectangle
             breadth->breadth of rectangle  
    '''
    # Approach : By calling the function  areaOfRectangle()
    length = int(input("Enter the length of rectangle: "))
    breadth = int(input("Enter the breadth of rectangle: "))
    area=areaOfRectangle(length,breadth)
    print('Area of rectangle is ',area)
    
if __name__ =="__main__":
    main()
