def first_n_smallest(arr, n):
        smallList = arr[:]
        while len(smallList) > n:
            maxNumber = max(smallList)
            smallList.reverse()
            smallList.remove(maxNumber)
            smallList.reverse()
                  
            
        return smallList