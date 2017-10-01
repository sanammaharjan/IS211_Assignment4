import time
import random

def sequential_search(listdata, item):
    '''
    It searches the given item into list of data by sequentially.
    :param listdata(list): data to search into.
    :param itemdata(mixed): item to search
    :return: Answer if it is found or not with total processing time.
    '''
    starttime = time.time()
    position = 0
    found = False

    while position < len(listdata) and not found:
        if listdata[position] == item:
            found = True
            break
        else:
            position += 1
    endtime = time.time()
    total_searchtime = (endtime - starttime)
    return total_searchtime, found


def ordered_sequential_search(listdata, item):
    '''
    It searches the given item into list of data by ordered sequentially.
    :param listdata:  data to search into.
    :param itemdata: item to search.
    :return: Answer if it is found or not with total processing time.
    '''
    listdata.sort() # order the list
    starttime = time.time()
    position = 0
    found = False

    while position < len(listdata) and not found:
        if listdata[position] == item:
            found = True
            break
        else:
            position += 1
    endtime = time.time()
    total_searchtime = (endtime - starttime)
    return total_searchtime, found

def binary_search_iterative(listdata, item):
    '''
    Function to perform binary search.
    :param listdata: data to search into.
    :param item: item to search
    :return: Answer if it is found or not with total processing time.
    '''
    listdata.sort()
    starttime = time.time()
    first = 0
    last = len(listdata) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if listdata[midpoint] == item:
            found = True
            break
        elif item < listdata[midpoint]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    endtime = time.time()
    total_searchtime = (endtime - starttime)
    return total_searchtime, found


def binary_search_recursive(listdata, item):
    '''
    Function to perform binary search recursively.
    :param listdata: data to search into.
    :param item: item to search
    :return: Answer if it is found or not with total processing time.
    '''
    # listdata = []
    listdata.sort()
    startime = time.time()
    if len(listdata) == 0:
        found = False
    else:
        midpoint = len(listdata) // 2
        if listdata[midpoint] == item:
            found = True
        elif item < listdata[midpoint]:
            return binary_search_iterative(listdata[:midpoint], item)
        else:
            return binary_search_iterative(listdata[midpoint + 1:], item)
    endtime = time.time()
    total_searchtime = (endtime - startime)
    return total_searchtime, found


def generate_random_list(x):
    '''
    Function to generation random number
    :param x(int): to specify no of random list to generate
    :return: list data
    '''
    list_value = []
    for i in range(x):
        list_value.append(random.randint(1, x))
    return list_value

def main():
    '''
    Main funciton which call other search function and generate the result
    :return: Print the answer of searches
    '''
    samp_number = [500, 1000, 10000]
    for i in samp_number:
        counter = 100 # counter to specify number of search to run
        result = [0, 0, 0, 0]  # empty list
        while counter > 0:
            list_value = generate_random_list(i)
            result[0] += sequential_search(list_value, -1)[0]
            result[1] += ordered_sequential_search(list_value, -1)[0]
            result[2] += binary_search_iterative(list_value, -1)[0]
            result[3] += binary_search_recursive(list_value, -1)[0]
            counter -= 1
        print 'Total Search time required in list of {} are:'.format(i)
        print ('    Sequential Search took %10.7f seconds to run, on average') % (result[0] / 100)
        print ('    Ordered Sequential Search took %10.7f seconds to run, on average') % (result[1] / 100)
        print ('    Iterative Binary Search took %10.7f seconds to run, on average') % (result[2] / 100)
        print ('    Recursive Binary Search took %10.7f seconds to run, on average') % (result[3] / 100)

if __name__ == "__main__":
    main()