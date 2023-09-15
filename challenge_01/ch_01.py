# The best way to do this in Python is to loop over the number sequence defined by the user and by
#each element test wether the condition is true or false, adding it's number to the total_sum variable.
def multiples_sum(up_to):
    total_sum=0
    if up_to>0 and up_to<1000:   
        for i in range(up_to):
            if i%3==0 or i%5==0:
                total_sum+=i
    return total_sum

#Now let's test the algorithm, in order to test faster, we will avoid a battery of unitary tests and test it 
# by using the print fuction instead, for harder problems we will use good test to verify our algorithms.
print(multiples_sum(10))
print(multiples_sum(13))
print(multiples_sum(15))