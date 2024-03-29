import time
import random


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def simulate_line(till_show, max_time):
    """
        Args:
            till_show int : this shows the time left till
                the movie starts
            
            max_time int: this represents the approximate time that
                a person might take to buy a ticket 
                
        Return:

    """
    
    pq = Queue()
    tix_sold = []
    
    
    for i in range(100):
        pq.enqueue("Person" + str(i))
    # From person 0 to person 99 in the line
    
    t_end = time.time() + till_show
    now = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r = random.randint(0, max_time)
        time.sleep(r)
        person = pq.dequeue()
        print(person)
        tix_sold.append(person)
        return tix_sold


sold = simulate_line(5, 1)
print(sold)
