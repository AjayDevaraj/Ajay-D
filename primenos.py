def main():
    pass

a=int(input())
b=int(input())
for n in range(a+1,b):
	 f=0
	 for i in range(2,n//2):
			 if n%i==0:
				 f=1
				 break
	 if f==0:
		 print(n)

if __name__ == '__main__':
    main()
