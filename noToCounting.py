def main():
    numbers={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'fourty',50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',100:'one hundred',200:'two hundred',300:'three hundred',400:'four hundred',500:'five hundred',600:'six hundred',700:'seven hundred',800:'eight hundred',900:'nine hundred',1000:'one thoushand',2000:'two thoushand',3000:'three thoushand',4000:'four thoushand',5000:'five thoushand',6000:'six thoushand',7000:'seven thoushand',8000:'eight thoushand',9000:'nine thoushand',10000:'ten thoushand'}
    userInput=int(input("Please Enter Any no."))
    word=''
    size=len(str(userInput))
    if userInput>20:
        while(size != 0):
            temp=int(userInput/10**(size-1))
            if temp>0:
                word=word+numbers[temp*10**(size-1)]+" "
            else:
                word=word
            userInput=userInput%10**(size-1)
            size=size-1
        print(word)
    elif userInput<-20:
        userInput=userInput*-1
        word='minus '
        while(size != 0):
            temp=int(userInput/10**(size-1))
            if temp>0:
                word=word+numbers[temp*10**(size-1)]+" "
            else:
                word=word
            userInput=userInput%10**(size-1)
            size=size-1
        print(word)
    else:
        if userInput<0:
            userInput=userInput*-1
            word='minus '+numbers[userInput]
            print(word)
        else:   
            print(numbers[userInput])
    
    
if __name__ =='__main__':
    main()
