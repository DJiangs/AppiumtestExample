import random
random.random
def bubble_sort(list):
    for i in range(0,len(list)):
        is_sorted=True
        for j in range(0,len(list)-i-1):
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
                is_sorted=False
        if is_sorted:
            return

list=[23,122,3,223,2,44,-12,23,222]
bubble_sort(list)
print(list)
print(hex(12))