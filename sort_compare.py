import time
import random

def insertion_sort(listdata):
    starttime = time.time()
    for y in range(1, len(listdata)):
        current_value = listdata[y]
        position = y
        while position > 0 and listdata[position - 1] > current_value:
            listdata[position] = listdata[position - 1]
            position -= 1
        listdata[position] = current_value
    endtime = time.time()
    total_sorttime = (endtime - starttime)
    return total_sorttime, listdata

def gap_insertion_sort(listdata, start, gap):
    starttime = time.time()
    for x in range(start + gap, len(listdata), gap):
        current_value = listdata[x]
        position = x
        while position >= gap and listdata[position - gap] > current_value:
            listdata[position] = listdata[position - gap]
            position -= gap
        listdata[position] = current_value

def shell_sort(listdata):
    starttime = time.time()
    sublist_count = len(listdata) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(listdata, start_position, sublist_count)
        sublist_count = sublist_count // 2
    endtime = time.time()
    total_sorttime = (endtime - starttime)
    return total_sorttime, listdata

def python_sort(listdata):
    startime = time.time()
    listdata = listdata.sort
    endtime = time.time()
    total_sorttime = (endtime - startime)
    return total_sorttime, listdata

def generate_random_list(x):
    list_value = []
    for i in range(x):
        list_value.append(random.randint(1, x))
    return list_value

def main():
    samp_number = [500, 1000, 10000]
    for i in samp_number:
        counter = 100 # counter to specify number of search to run
        result = [0, 0, 0]  # empty list
        while counter > 0:
            list_value = generate_random_list(i)
            result[0] += insertion_sort(list_value)[0]
            result[1] += shell_sort(list_value)[0]
            result[2] += python_sort(list_value)[0]
            counter -= 1
        print 'Total sort time required in list of {} are:'.format(i)
        print ('    Insertion Sort took %10.7f seconds to run, on average') % (result[0] / 100)
        print ('    Shell Sort took %10.7f seconds to run, on average') % (result[1] / 100)
        print ('    Python took %10.7f seconds to run, on average') % (result[2] / 100)

if __name__ == "__main__":
    main()