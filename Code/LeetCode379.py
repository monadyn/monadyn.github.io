import sys

#可以构造一棵完全二叉树，最后一层的叶子节点表示1~max_id，树上每个节点使用一个标记位full表示以它为跟的子树是否全部分配完。由于是完全二叉树，可以使用堆的索引方式实现。
#分配和销毁都是单点的，因此沿着叶子到跟的路径更新full标记即可

#1)queue + set 的方法alloc和dealloc 时间复杂度都是O（1），虽然空间复杂度是O（N），但是实际的memory footprint大于bitset
#2)bitset省空间，但是alloc的复杂度是O（N）
#3)segment tree则是折中，alloc和dealloc都是O（lgN）,而且memory footprint小于queue+set
#都是tradeoff，要看实际情况选用哪种方案

class PhoneDirectory3(object):
    def __init__(self, maxNumbers):
        #The bit array holds the state of each id, 
        #the front of the queue has the available ID. O(n) time, O(n) space
        self.__curr = 0 #pointer hold current available id
        self.__numbers = [i for i in range(maxNumbers)]
        self.__used = [False] * maxNumbers#bit array
        print(self.__numbers, sys.getsizeof(self.__numbers)//len(self.__numbers), sys.getsizeof(self.__used))
    def get(self):#allocate
        if self.__curr == len(self.__numbers):
            return -1#error handling
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number
    def check(self, number):
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]
    def release(self, number):#deallocate
        #error handling
        if not 0 <= number < len(self.__numbers) or \
           not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__number
# init:     Time: O(n), Space: O(n)
# get:      Time: O(1), Space: O(1)
# check:    Time: O(1), Space: O(1)
# release:  Time: O(1), Space: O(1)
class PhoneDirectory1(object):
    def __init__(self, maxNumbers):
        self.__curr = 0 #pointer hold current available id
        self.__numbers = [i for i in range(maxNumbers)]
        self.__used = [False] * maxNumbers#bit array
        print(self.__numbers, sys.getsizeof(self.__numbers)//len(self.__numbers), sys.getsizeof(self.__used))
    def get(self):#allocate
        if self.__curr == len(self.__numbers):
            return -1#error handling
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = True
        return number
    def check(self, number):
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]
    def release(self, number):#deallocate
        #error handling
        if not 0 <= number < len(self.__numbers) or \
           not self.__used[number]:
            return
        self.__used[number] = False
        self.__curr -= 1
        self.__numbers[self.__curr] = number

class PhoneDirectory2(object):
    def __init__(self, maxNumbers):
        self.__curr = 0
        self.__numbers = [i for i in range(maxNumbers)]
        self.__used = bytearray(maxNumbers) #bit array
        print(self.__numbers, sys.getsizeof(self.__numbers)//len(self.__numbers), sys.getsizeof(self.__used), self.__used)
        #print('bytes')
        #for i in range(len(self.__numbers)): print(self.__used[i])
    def get(self):#allocate
        if self.__curr == len(self.__numbers):
            return -1
        number = self.__numbers[self.__curr]
        self.__curr += 1
        self.__used[number] = ord('1')
        print('allocate:', self.__numbers, self.__used)
        return number
    def check(self, number):
        return 0 <= number < len(self.__numbers) and \
               not self.__used[number]
    def release(self, number):#deallocate
        if not 0 <= number < len(self.__numbers) or \
           self.__used[number] == ord('0'):
            return
        self.__used[number] = ord('0')
        self.__curr -= 1
        self.__numbers[self.__curr] = number
        print('release:', self.__numbers, self.__used)

n = 3
for directory in [PhoneDirectory1(n), PhoneDirectory2(n)]:
#for directory in [PhoneDirectory(n)]:
    #directory = PhoneDirectory(3)
    print(directory.get())
    print(directory.get())
    #print(directory.check(2))
    print(directory.get())
    print(directory.get())
    #print(directory.check(2))
    print(directory.release(1))
    #print(directory.check(1))
    #print(directory.check(2))
    print(directory.get())

class Bitmap:
    def __init__(self,max):
        #'Determine the number of arrays required'
        self.size = int((max + 31-1) / 31)
        print(max, self.size)
        self.array = [0 for i in range(self.size)]
 
    def bitindex(self,num):
        '''bit index, the remainder of this method is to determine the specific number of in a certain array '''
        return  num % 31

    def set(self,num):
        '''After calculating which number in a bitmap corresponds to a number, you need to set the corresponding position to 1'''
        '''#Just determine which number to calculate is in which array '''
        elemindex = num // 31
        '''# indicates the bit index of the calculation number '''
        byteindex = self.bitindex(num)
        '''#Select which array to operate on'''
        elem = self.array[elemindex]
        # ,Set the operation, 1 moves the byteindex bit to the left
        self.array[elemindex] = elem | (1 << byteindex)

    def test(self,i):
        '''#judge the corresponding number on the first array '''
        elemindex = i // 31
        '''#Position index '''
        byteindex = self.bitindex(i)
        '''#Logic and operation, to determine whether a bit is not in the bitmap, if it means that it should be taken out and traversed, the position where 1 appears when traversing, the number at this position is converted to decimal and then taken out. Traverse the generation of the sorting sequence '''
        if self.array[elemindex] & (1 << byteindex):
            return True
        return False
 
if __name__ == "__main__":
    ''' convert z to the largest number of 'assci'''
    MAX = ord('z')
    suffle_array = [x for x in 'coledraw']
    result = []
    '''# Call this class and pass the maximum number to it. Generate bit chart '''
    bitmap = Bitmap(int(MAX))
 
    '''Trouble through this array '''
    for c in suffle_array:
        bitmap.set(ord(c))
    for i in range(int(MAX) + 1):
        if bitmap.test(i):
            result.append(chr(i))
 
    print("Original array: %s" % suffle_array)
    print("sorted array: %s" % result)
