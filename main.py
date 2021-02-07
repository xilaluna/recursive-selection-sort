def list_sorted(lst, i, length):
    if i == length or lst[0] == None:
        return lst
    else:
        smallest_num = findSmallestNum(lst, i, length, i)
        temporary = lst[i]
        lst[i] = smallest_num
        print(smallest_num)
        lst[smallest_num] = temporary
        return list_sorted(lst, i+1, length)


def findSmallestNum(lst, j, length, small_num):
    if j == length:
        return small_num
    if lst[j] < list[small_num]:
        small_num = j
    return findSmallestNum(lst, j+1, length, small_num)


def list_form(lst):
    return list_sorted(lst, 0, len(lst))


list_form([1, 2, 3])
