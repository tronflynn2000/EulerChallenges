#We couldn't find any better solution for the problem. If we wanted to calculate the n-th term in the sequence,
#we would have used different algorithms such as matrix exponentiation, but we needed each number we got in
#the entire sequence to add all the even values, having a complexity of O(n).

def fibo_calc(n):
    num1=0
    num2=1
    num3=0
    sum=0
    while num3<=n:
        num3=num1+num2
        if num3%2==0:
            sum=sum+num3
        num1=num2
        num2=num3
    return sum
print(fibo_calc(4000000))