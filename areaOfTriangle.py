def areaOfTriangle(height,base):
    '''
    Objective: To print a area of triangle using user input height & base
    Input Parrameter: 
             height->height of triangle
             breadth->base of triangle
    Result : Area of triangle
    '''
    #Approach : area=1/2*height*base
    
    area = (height*base)/2
    return area

def main():
    '''
    Objective: To print a area of triangle using user input height & base
    Input Parrameter:
             height->height of triangle
             breadth->base of triangle  
    '''
    # Approach : By calling the function  areaOfTriangle()
    height = int(input("Enter the height of triangle: "))
    base = int(input("Enter the base of triangle: "))
    area=areaOfTriangle(height,base)
    print('Area of Triangle is ',area)
    
if __name__ =="__main__":
    main()
