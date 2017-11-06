def insert_element(element,list,lengthOfList):
    '''
    Objective        : To insert an element into a sorted list by recursion 
    Input Parameters : 
             Element -> element to be entered by user
               length -> store temprorily  length of the list
     Result:element insert as a sorted manner
   
    '''
    #Approach  :  Recursivly
    length=lengthOfList-1
    if(length==0 and element<list[0]):
        list.insert(0,element)
    elif(length==0 and element>list[0]):
        list.insert(1,element)
    elif(element<list[length]):
        insert_element(element,list,length)   
    else:
        list.insert(length+1,element)
       
def main():
    '''
    Objective        : To insert an element into a sorted list by recursion  
    Input Parameters : 
               list-> containig list of element
               lengthOfList-> length of list
               element -> element enter by user
    '''
    # Approach : Call the function  insert_element()

    list=[12,22,51,65,98,123,128,488,899,998,6578]
    lengthOfList=len(list)
    element = int(input("Enter the Element : "))
    insert_element(element,list,lengthOfList)
    print(list)
   

if __name__ == '__main__':
    main()
