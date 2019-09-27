# this comment is just to test to see if connected to github
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError("List is None")
    elif len(int_list) == 0:
        return None
    else:
        max_val = int_list[0]
        for i in range(len(int_list)):
            if int_list[i] > max_val:
                max_val = int_list[i]
        return max_val


def reverse_rec(int_list):  # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
    if int_list == None:
        raise ValueError("List is None")
    else:
        if len(int_list) == 0:
            return int_list
        return reverse_rec(int_list[1:]) + ([int_list[0]])


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
    if int_list == None:
        raise ValueError("List is None")
    if len(int_list) == 0:
        return None
    else:
        mid = ((high + low) // 2)
        if (mid == high and int_list[mid] != target) or (mid == low and int_list[mid] != target):
            return None
        if target == int_list[mid]:
            return mid
        elif int_list[mid] > target:
            return bin_search(target, low, mid - 1, int_list)
        elif int_list[mid] < target:
            return bin_search(target, mid + 1, high, int_list)
