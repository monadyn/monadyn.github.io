from typing import List

def fill_the_truck(num: int, boxes: List[int], unit_size: int, unitsPerBox: List[int], truck_size: int) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    max_u = 0
    i = 0
    for (u,b) in sorted(zip(unitsPerBox,boxes),reverse=True):
        if i+b <= truck_size:
            max_u += u*b
            i += b
        elif i+b > truck_size and i < truck_size:
            max_u += u*(truck_size-i)
            i = truck_size
        else: 
            break
        
    return max_u

if __name__ == '__main__':
    num = int(input())
    boxes = [int(x) for x in input().split()]
    unit_size = int(input())
    units_per_box = [int(x) for x in input().split()]
    truck_size = int(input())
    res = fill_the_truck(num, boxes, unit_size, units_per_box, truck_size)
    print(res)

