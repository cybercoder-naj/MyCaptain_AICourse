def sort(arr):
    if len(arr) > 1:
        m = len(arr) // 2
        left = arr[:m]
        right = arr[m:]

        sort(left)
        sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            elif left[i] > right[j]:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


if __name__ == '__main__':
    array = list(map(int, input().split()))

    print('Sorted array')
    sort(array)
    print(array)
