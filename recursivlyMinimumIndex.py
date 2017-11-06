def minElementIndex(list,lowerIndex,upperIndex,minIndex):
    '''
    Objective: To return a index of minimum value of given area in list 
    Input Parameters : 
            lowerIndex-> containing the lower index
            upperIndex-> containing the upper index
            minIndex-> containing the minimum  index
            Return: index of minimum value 
    '''
    #Approach : Recursive
    if(lowerIndex==upperIndex):
        return minIndex
    elif(lowerIndex<upperIndex):
        if(list[minIndex]>list[lowerIndex]):
            minIndex=lowerIndex
            return minElementIndex(list,lowerIndex+1,upperIndex,minIndex)
        else:    
            return minElementIndex(list,lowerIndex+1,upperIndex,minIndex)
            
    
def main():
    '''
    Objective : To print a index of minimum value of given area in list  
    Input Parameters : 
            lowerIndex-> containing the lower index
            upperIndex-> containing the upper index
            minIndex-> containing the minimum  index
    '''
    # Approach : Call the function  minElementIndex()
    list=[12,22,65,4,54,8,89,656,98,23]  
    lowerIndex=0
    upperIndex=5
    minIndex=5
    minIndex=minElementIndex(list,lowerIndex,upperIndex,minIndex)
    print("Minimum Index Is : ",minIndex," and its value is: ",list[ minIndex])

    
if __name__ == '__main__':
    main()
