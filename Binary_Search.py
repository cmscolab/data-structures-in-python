def binary_search(input_array, val_to_be_searched):
    low = 0
    high = len(input_array) - 1
    while(low <= high):
        mid = (low + high)/2
        if input_array[mid] == val_to_be_searched:
            return mid
        elif input_array[mid] < val_to_be_searched:
            low = mid + 1
        else:
            high = mid - 1
    return -1

if __name__ == "__main__":
    test_list = [1, 2, 5, 6, 8, 9, 12]
    val = 9
    invalid_val = 13
    print(binary_search(test_list, val))
    print(binary_search(test_list, invalid_val))
