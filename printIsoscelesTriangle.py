def triangle(c):
    '''
    Objective: To print a triangle using user input 
    Input Parrameter: 
             c->user input character
    Result : printed triangle of row size 4
    '''
    #Approach :using print() function
    print("    ",c,"    ")
    print("   ",c,c,"   ")
    print("  ",c,c,c,"  ")
    print(" ",c,c,c,c," ")
    
   

def main():
    '''
    Objective: To print a triangle using user input
    Input Parrameter:
             character->user input character
    '''
    # Approach : By calling the function  triangle()
    character = input("Enter the character for triangle: ")
    triangle(character)
    
if __name__ =="__main__":
    main()
