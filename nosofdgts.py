def main():
    pass
count = 0
number = int(input("Enter a number "))
while (number > 0):
  number = number//10
  count = count + 1
print ("Total number of digits : ",count)
if __name__ == '__main__':
    main()
