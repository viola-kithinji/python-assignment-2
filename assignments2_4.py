#define the input
#define the output
#define the relations/operations
#result=num
#result=result*num
#20*20*20*20
#result=result*20=(20*20=400)0
#result= result*20=(400*20=8000)1
#result= result*20=(8000*20=16000)2

def main():
    num=int(input("enter a whole number"))#20
    exponent=int(input("enter exponent number"))#4
    
    result=num

    
    for i in range(3):
        result=result*num

        
        print(result)


main()
                
    
                
    
