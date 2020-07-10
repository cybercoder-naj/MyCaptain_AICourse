def sort(arr, low, high):
    if low < high:
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[high], arr[i + 1] = arr[i + 1], arr[high]
        pi = i + 1

        sort(arr, low, pi - 1)
        sort(arr, pi + 1, high)


if __name__ == '__main__':
    array = list(map(int, input().split()))
    sort(array, 0, len(array) - 1)
    print('Sorted Array', array)
