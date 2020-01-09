def sparse_search(data, search_val):
    print("Data: {}".format(str(data)))
    print("Search Value: {}".format(str(search_val)))

    first = 0
    last = len(data) - 1

    while first <= last:
        mid = (first + last) // 2

        if not data[mid]:
            left = mid - 1
            right = mid + 1

            while (True):
                if left < first and right > last:
                    print("{} is not in the dataset".format(search_val))
                    return