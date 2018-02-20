def main():
    n=int(input("Enter number:"))
    temp=n
    rev=0
    while(n>0):
        dig=n%10
        rev=rev*10+dig
        n=n//10
    if(temp==rev):
        print("The number Yes")
    else:
        print("The number No")


if __name__ == '__main__':
    main()
