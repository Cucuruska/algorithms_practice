# merge sort
# 6n * (log2(n) + 1)

def merge_sort(array): 
    n = len(array)

    if n > 1:
        m = n/2
        a = merge_sort(array[0:m])
        b = merge_sort(array[m:n])
        i = 0 # iterator over 'a' array
        j = 0 # iterator over 'b' array
        res = []

        for k in range(0,n):
            if i >= len(a):
                res.extend(b[j:])
                break
            elif j >= len(b):
                res.extend(a[i:])
                break
            else:
                if a[i] < b[j]:
                    res.append(a[i])
                    i += 1
                else:
                    res.append(b[j])
                    j += 1
        return res
    else:
        return array

if __name__ == '__main__':
    print merge_sort([1,9,5,2,6,7,3])
    print merge_sort([])
