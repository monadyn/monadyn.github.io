from threading import Condition,Lock,Thread
from threading import current_thread
class ZeroEvenOdd:
    def __init__(self, n):
        self.lock = Lock()
        self.n = n
        self.i = 0
        self.zero_cv = Condition(self.lock)
        self._cv = Condition(self.lock)
        
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i < self.n:
            with self.lock:
                printNumber(0)
                #print('0')
                if self.i == 0: self.i = 1
                self.zero_cv.notify_all()
                print('wait..')
                self._cv.wait()
        
    def even(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i<= self.n:
            with self.lock:
                while self.i ==0 or self.i % 2:
                    self.zero_cv.wait()
                printNumber(self.i)
                #print(self.i)
                self.i += 1
                self._cv.notify()
                
    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        while self.i<= self.n:
            with self.lock:
                while self.i ==0 or not self.i % 2:
                    self.zero_cv.wait()
                printNumber(self.i)
                #print(self.i)
                self.i += 1
                self._cv.notify()    

def printNumber(i):
    #print(current_thread.get_name(),i)
    print("\n{0} {1}".format(current_thread().getName(), i), flush=True)

s = ZeroEvenOdd(2)
Thread1 = Thread(target=s.zero, name="t-1", args=(printNumber,), daemon=0)
Thread2 = Thread(target=s.even, name="t-2", args=(printNumber,), daemon=0)
Thread3 = Thread(target=s.odd,  name="t-3", args=(printNumber,), daemon=0)
 
Thread1.start()
Thread2.start()
Thread3.start()

