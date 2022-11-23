def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1


if __name__ == '__main__':
    my_list = [1, 2, 4, 5, 7, 6]

    print(binary_search(my_list, 7))
