# Write program to play ‘Memory Game’ with the user. In this
# game you are required to take n numbers as input from the user and
# after taking all the numbers your program must display the largest and
# the smallest number entered by the user. (Hint: Use Loop and if
# conditions)
n = int(input('How many numbers you want to Enter: '))
my_list=[]
if n<0:
    print('enter a positive number')
elif n==1:
    print('not sufficient numbers')
else:
    for i in range (1,n+1):
        x = int('Input ',i,'th number: ')
        my_list.append(x)
print('Maximum number is :',max(my_list))
print('Maximum number is :',min(my_list))


    



