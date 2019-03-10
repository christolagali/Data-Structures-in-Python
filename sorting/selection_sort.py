

# This method will pick the maximum and move it to the last part
def selecSortMax(arr):

    # n no passes
    for n in range(len(arr)-1,0,-1):

        # get the Sub array to be sorted
        sub_array = arr[0:n+1]

        # find the max value
        max_value = max(sub_array)

        # find the index of the max_value
        max_index = sub_array.index(max_value)

        if arr[n] != max_value:

            # perform swap
            tmp = arr[n]
            arr[n] = arr[max_index]
            arr[max_index] = tmp
    
    return arr

    



# This method will pick the minimum from the list place it to the first part
def selecSortMin(arr):

    for n in range(len(arr)-1,0,-1):

        k= (len(arr)-1) - n
        # get a sub array to find minimum element and exclude sorted indexes
        sub_array = arr[k:len(arr)]

        # find the minimum value
        min_value = min(sub_array)

        # find the index of the minimum element
        min_value_index = arr.index(min_value)
        print(arr)
        
        if arr[k] != min_value:

            tmp = arr[k]
            arr[k] = arr[min_value_index]
            arr[min_value_index] = tmp
    
    return arr

    



arr = [7,10,2,5,11]
#print(selecSortMax(arr))

print(selecSortMin(arr))