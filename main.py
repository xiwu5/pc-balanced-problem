def balanced(numbers):
    ans = set()
    sum_map = {}
    final = set()
    # value_list = []

    if_appear = set()

    for i in range(len(numbers) - 1): #  avoid index out of boundary issue
        for j in range(i + 1, len(numbers)):
            sum = numbers[i] + numbers[j]
            if sum in sum_map:
                sum_map[sum].append(numbers[j])  # Key exists, append to list
                sum_map[sum].append(numbers[i])
            else:
                sum_map[sum] = [numbers[j],numbers[i]] # 13, 7, 8... # store the sum as the key instead
            # handle case: when add the sum again, do not update value but add on value
            sum = 0

    for key, value in sum_map.items():
        # print("test", len(value))
        # print(value)
        if len(value) > 2:
            ans.add(value)
            #list(set(list))

    #final.add(ans)
    
    return ans
    # # iterate the map, when their value are equal, store the key
    # for value in sum_map.values():
    #     # find if any values are equal, return true, otherwise return set()
    #     value_list.append(value)
    
    # # loop through the value list, to check if any values are equal
    # first = value_list[0]
    # second = first + 1

    # while second <= (len(value_list) - 1):
    #     if value_list[first] == value_list[second]:
    #         for key, value in sum_map.items():
    #             if value == value_list[first]:
    #                 ans.append(key)



# order doesn't matter
# brute force:
    # map : 3 key - the addition of i numbers
        #  5 key - 2(7), 14(19) # not to store the second number, store their sum as the value
        # use the second num as the key, their sum as value
    
    # how i get 3 + 4 = 5 + 2
        # browse values of the map, find the equal values
            # get a list of the values from the map
            # use for loop to get the pair - return set(pairs)
            # return set()



assert balanced([3, 10, 4, 5, 2, 14]) == set([3, 2, 4, 5])

assert balanced([60, 0, 10, -35, 90]) == set()

assert balanced([]) == set()

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
