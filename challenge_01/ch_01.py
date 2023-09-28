from threading import Thread


class CustomThread(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self,group,target,name,args,kwargs)
        self._returnValue=None

    def run(self):
        if self._target is not None:
            self.returnValue = self._target(*self._args, **self._kwargs)

    def join(self):
        Thread.join(self, *self._args)
        return self._return


# The best way to do this in Python is to loop over the number sequence defined by the user and by
#each element test wether the condition is true or false, adding it's number to the total_sum variable.
def multiples_sum(up_to):
    total_sum=0
    if up_to>0 and up_to<=1000000000:   
        for i in range(up_to):
            if i%3==0 or i%5==0:
                total_sum+=i
    return total_sum

#Now let's test the algorithm, in order to test faster, we will avoid a battery of unitary tests and test it 
# by using the print fuction instead, for harder problems we will use good test to verify our algorithms.
print(multiples_sum(10))
print(multiples_sum(13))
print(multiples_sum(15))
#print(multiples_sum(1000000000))

# When we solved the problem we found a better way to do this using some Set theory along with some
# basic hardware knowledge. We could sum all numbers divisible by 5 with all numbers divisible by 3
# and then substract the numbers divisible by 15, which will be doubled. We can do those 3 operations
# using different threads, this way we could optimize our algorithm.

def modulo_three_sum(up_to):
    total_sum=0
    if up_to>0 and up_to<=1000000000:   
        for i in range(up_to):
            if i%3==0:
                total_sum+=i
    return total_sum

def modulo_five_sum(up_to):
    total_sum=0
    if up_to>0 and up_to<=1000000000:   
        for i in range(up_to):
            if i%5==0:
                total_sum+=i
    return total_sum

def modulo_fifteen_sum(up_to):
    total_sum=0
    if up_to>0 and up_to<=1000000000:   
        for i in range(up_to):
            if i%15==0:
                total_sum+=i
    return total_sum

def example_function():
    total_sum=0
    three=Thread(target=modulo_three_sum, args=1000000000)
    three.start()
    five=Thread(target=modulo_five_sum, args=1000000000)
    five.start()
    fifteen=Thread(target=modulo_fifteen_sum, args=1000000000)
    fifteen.start()
    three.join()
    five.join()
    fifteen.join()

    total_sum=three+five-fifteen
    return total_sum

print(example_function())