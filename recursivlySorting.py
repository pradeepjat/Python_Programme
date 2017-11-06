def maxElementIndex(list,length,index):
    '''
    Objective        : To return a index of maximum value of list 
    Input Parameters : 
            length -> containing the length of list
            index-> store a  index of maximum value of list
            Return: index of maximum value of list
    '''
    #Approach : Recursive
    if(length>0):
        if(list[index]<list[length-1]): 
            index=length-1
            return maxElementIndex(list,length-1,index)
        else:
            return maxElementIndex(list,length-1,index)
    else:
        return index
    
def sorting(list,length):
    '''
    Objective        : To sorting a list by recursion 
    Input Parameters : 
            maximum -> Store a index of maximum value in a list
            index-> Temprory store a last index
            temp -> temprory variable that use for swaping
     Return:Sorted list
    '''
    #Approach Recrsivly Swap the maximum value with the last index of list
    temp=0;
    if(length>0):
        index=length-1
        maximum=maxElementIndex(list,length,index)
        if(list[length-1]<list[maximum]):
            temp=list[maximum]
            list[maximum]=list[length-1]
            list[length-1]=temp
            return sorting(list,length-1)
        else:
            return sorting(list,length-1)
    
    else:
        return list   
        

def main():
    '''
    Objective : Sorting by recursion  
    Input Parameters : 
               list-> containig list of element
               length-> length of list
    Result: Sorted list               
    '''
    # Approach : Call the function  sorting()
    list=[12,4,241,48,54,544,78,55,20]
    length=len(list)
    print(sorting(list,length))

if __name__ == '__main__':
    main()
