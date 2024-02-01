def sum_of_products(list1, list2):
    if len(list1) != len(list2):
        return ('Error')
    counter = 0
    sum = 0
    for num in list1:
        sum += (num * list2[counter])
        counter += 1
    return sum

    # if len(list1) == len(list2):
    #     print(sum_of_products(list1, list2))

if __name__ == '__main__':
    input1 = str(input())
    input2 = str(input())
    
    list1_string = input1.split()
    list2_string = input2.split()
    
    list1 = []
    list2 = []

    #comment

    for digit in list1_string:
        list1.append(int(digit))
    for digit in list2_string:
        list2.append(int(digit))

    print(sum_of_products(list1, list2))

