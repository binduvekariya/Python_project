def binary_serch(list,element):
    steps = 0
    start = 0 
    end = len(list)
    middle = 0

    while(start<=end):
        print("steps ",steps,":",str(list[start:end+1]))
        steps = steps + 1
        middle = (start+end)//2

        if(element==list[middle]):
            return middle
        elif(element<list[middle]):
            end = middle - 1
        else:
            start = middle + 1

    return -1


list = [1,2,3,4,5,6,7,8,9,10]
element = 3
binary_serch(list,element)