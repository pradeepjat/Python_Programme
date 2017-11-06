def percentage(marks_obtained,max_marks):
    '''
    Objective: To find a percentage by user input marks obtatained and maximum marks
    Input Parrameter: 
             marks_obtained->contain marks obtained by user
             max_marks->contain maximum marks 
    Return : percentage
    '''
    #Approach : percentage = (marks_obtained/max_marks)*100
    
    calculated_percentage = (marks_obtained/max_marks)*100
    return calculated_percentage

def main():
    '''
    Objective: To find a percentage by user input marks obtatained and maximum marks
    Input Parrameter:
             marks_obtained->contain marks obtained by user
             max_marks->contain maximum marks  
    Output Parrameter: 
             calculated_percentage -> contain final percentage
    '''
    # Approach : By calling the function  percentage()
    
    marks_obtained = int(input("Enter marks obtained: "))
    max_marks = int(input("Enter maximum marks: "))
    calculated_percentage= percentage(marks_obtained,max_marks)
    print('your percentage : ',calculated_percentage,'%')
    
if __name__ =="__main__":
    main()
