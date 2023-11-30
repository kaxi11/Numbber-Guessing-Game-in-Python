 import random

r = random.randint(1,20)



while(True):

    n = int(input())

    if(n>r):

        print(" Worong ! Please try a Smaller number")

    elif(n<r):

        print("Wrong ! Try a greater number")

    else:

        print("Congrats You Guess the right nuumber")

        break;
