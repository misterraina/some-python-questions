numb = int(input('Enter a number: '))
sum = 0
n = len(str(numb))
temp = numb

while(numb > 0):
    digit = numb % 10
    sum = digit ** n + sum
    numb = numb // 10
# print(f'{temp} and {sum}')
if (temp == sum):
    print(True,'Arnstrong')
else:
    print(False,'Arnstrong')