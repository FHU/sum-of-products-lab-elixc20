
def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        print("error")
        return None
    
    __name__ = sum(a * b for a, b in zip(list1, list2))
    return __name__

list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
__name__ = sum_of_products(list1, list2)

if __name__ is not None:
   print(__name__)