num = input("entre com um numero: ")
if ((num <= 0) or (num == 1)):
    print(num,"nao eh numero primo")
elif (num > 1):
    for i  in range(2,num):
        if(num % i):
            print(num,"nao eh numero primo")
    else:
        print(num,"eh numero primo")