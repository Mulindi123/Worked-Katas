def solution(blocks):
    n = len(blocks)
    maximum_distance = 0

    # loop through the array i (length = n)
    for i in range(n):
        current_distance = 0

        for left_side in range(i, 0, -1):
            if blocks[left_side-1] < blocks[left_side]:
                break
            current_distance += 1

        for right_side in range(i, n-1):
            if blocks[right_side+1] < blocks[right_side]:
                break
            current_distance += 1
        
        # import ipdb; ipdb.set_trace()

        maximum_distance = max(current_distance, maximum_distance)
        # print(max_distance)

    return maximum_distance+1
    # current_distance to zero
    # Loop left side, i, -1

    # Loop right side i, n-1

# print(solution([1, 5, 5, 2, 6]))
# print(solution([2, 6, 8, 5]))    # output 4
# print(solution([1, 1]))

# def solution(blocks):
#     n = len(blocks)
#     max_distance = 0

#     for i in range(n):
#         for j in range(i, n):
#             if blocks[j] >= blocks[i]:
#                 max_distance = max(max_distance, j - i)

#     return max_distance

# # Test the function
# blocks = [2, 6, 8, 5]
# #print(solution(blocks))  # Output: 3
# print(solution([1, 5, 5, 2, 6]))


def solution(blocks):
    N = len(blocks)

    #creating an array to stor the maximum distance for each starting block
    max_distance = [0] * N

    for i in range(N):
        max_left =i
        max_right =i

        #left movement
        while max_left >0 and blocks[max_left-1] >=blocks[max_left]:
            #right movement 
            max_left-=1
        while max_right<N-1 and blocks[max_right+1] >=blocks[max_right]:
            max_right += 1
            max_distance[1] = max_right - max_left + 1

    return max(max_distance)




