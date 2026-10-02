array = [35,12,58,21,46,7]

# find the minimum value
def FindMin():
    small = array[0]
    for i in range (1,len(array)):
        if array[i]<small:
            small = array[i]

    print(small)
        

# ascending order
def Asc():
    
    for i in range (len(array)):
        minIndex = i

        for j in range (i+1,len(array)):
            if array[minIndex]>array[j]:
                minIndex = j
        
        array[minIndex],array[i] = array[i], array[minIndex]

    print(array)

Asc()




# descending order
def Desc():
    for i in range (len(array)):
        minIndex = i

        for j in range (i+1,len(array)):
            if array[minIndex]<array[j]:
                minIndex = j
        
        array[minIndex],array[i] = array[i], array[minIndex]

    print(array)



# select sort using min
def minSort():
    mini = min(array)
    print(mini)

