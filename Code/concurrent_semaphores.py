import random, time
from threading import BoundedSemaphore, Thread

max_items = 5

"""
Consider 'container' as a container, of course, with a capacity of 5
items. Defaults to 1 item if 'max_items' is passed.
"""
container = BoundedSemaphore(max_items)

def producer(n):
    print('producer %s' % n)
    for i in range(n):
        time.sleep(random.randrange(2,5))
        print('\t', time.ctime(), end=': ')
        try: 
            container.release() # increases ticket per release() call
            print("\tProduced a ticket .")
        except ValueError:
            print('\tproducer container full, can not increases ticket per release()')

def consumer(n):
    print('consumer %s' % n)
    for i in range(n):
        time.sleep(random.randrange(2,5))
        print(time.ctime(), end=': ')
        """
        In the following if statement we disable the default
        blocking behaviour by passing False for the blocking flag.
        """
        if container.acquire(False):
            print("Consumed a ticket by calling acquire().")
        else:
            print("empty, no ticket.")

threads = []
n = 5 #random.randrange(3,6)
print("starting with %s tickets in a container, %s available positions in the container" % (max_items,max_items))
#threads.append(Thread(target=consumer, args=(n,)))
threads.append(Thread(target=consumer, args=(random.randrange(n, n+max_items+2),)))
threads.append(Thread(target=producer, args=(n,)))

for thread in threads:
    thread.start()
for thread in threads: #Waits for threads to complete before moving on with the main script.
    thread.join()
print("done")

