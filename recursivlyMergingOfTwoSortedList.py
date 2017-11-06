def mergeSortedList(list1,list2,list3,lower1,lower2,upper1,upper2):
    '''
    Objective : Merge two Sorted list by recursion  
    Input Parameters : 
               list1-> containig first sorted list
               lower1-> lower index of first list
               upper1-> upper index of first list
               list2-> containig second sorted list
               lower2-> lower index of second list
               upper2-> upper index of second list
    Result: third list which is Merging of two Sorted list      
    '''
    # Approach : recursive
    if(lower1<upper1 and lower2<upper2):
        if(list1[lower1]<list2[lower2]):
            list3.append(list1[lower1])
            return mergeSortedList(list1,list2,list3,lower1+1,lower2,upper1,upper2)
        else: 
            list3.append(list2[lower2])
            return mergeSortedList(list1,list2,list3,lower1,lower2+1,upper1,upper2)        
    elif(lower1<upper1 and lower2==upper2):
        list3.append(list1[lower1])
        return mergeSortedList(list1,list2,list3,lower1+1,lower2,upper1,upper2)
        
    elif(lower1==upper1 and lower2<upper2):
        list3.append(list2[lower2])
        return mergeSortedList(list1,list2,list3,lower1,lower2+1,upper1,upper2)
        
    elif(lower1==upper1 and lower2==upper2):
        return list3
def main():
    '''
    Objective : Merge two Sorted list by recursion  
    Input Parameters : 
               list1-> containig first sorted list
               lower1-> lower index of first list
               upper1-> upper index of first list
               list2-> containig second sorted list
               lower2-> lower index of second list
               upper2-> upper index of second list
    Result: third list which is Merging of two Sorted list      
    '''
    # Approach : Call the function  mergeSortedList()
    list1=[12,15,41,48,54,55,78,55]
    upper1=len(list1)
    lower1=0
    list2=[1,16,48,49,64,87,92,95]
    upper2=len(list2)
    lower2=0
    list3=[]
    list3=(mergeSortedList(list1,list2,list3,lower1,lower2,upper1,upper2))
    print(list3)
    print(list3)
if __name__ == '__main__':
    main()
