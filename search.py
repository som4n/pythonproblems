'''You are given an integer T (number of test cases). 
You are given array A and an integer B for each test case. 
You have to tell whether B is present in array A or not.'''

def main():
    
    t=int(input())
    while t>0:
        t-=1
        a=list(map(int,input().split()))
        length=a.pop(0)
        b=int(input())
        count=False
    
        for i in a:
            if i==b:
                count=True
        
        if count:
            print("1")
        else:
            print("0")           

if __name__ == '__main__':
    main()