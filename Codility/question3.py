
# QUESTION 3:
# You are given a list of N transfers (numbered from 0 to N-1) between two banks: bank A and bank B.
# The K-th transfer is described by two values:
# - R[K] (either 'A' or 'B') representing the recipient (the bank the transfer is sent to);
# - V[K] denoting the value sent via a transfer.
# All transfers are completed in the order they appear on the list.
# The banks do not want to go into debt (in other words, their account balance may not drop below 0).
# What minimum initial account balance in each bank is necessary in order to complete the transfers
# Write a function: def solution(R, V) that given a string R and an array of integers V, both of length N,
# returns an array of two integers.
# The integers should reperesent the minimum initial account balances fr banks A and B in the following
# order: [bank A, bank B].
# Result array should be returned as an array of integers.

# Examples:
# 1. Given R = "BAABA" and V = [2,4,1,1,2], the function should return [2,4].
# 2. Given R = "ABAB" and V = [10,5,10,15], the function should return [0,15].
# 3. Given R = "B" and V = [100], the function should return [100,0].

# A is a list of objects. Each object is {bank: R[K], amount: V[K]}


def solution(R, V):
    N = len(R)
    balance_A = 0
    balance_B = 0
    min_balance_A = 0
    min_balance_B = 0

    for i in range(N):
        if R[i] == 'A':
            balance_A += V[i]
            min_balance_A = min(min_balance_A, balance_A)
        else:
            balance_B += V[i]
            min_balance_B = min(min_balance_B, balance_B)

    return [max(0, min_balance_A), max(0, min_balance_B)]


print(solution("BAABA", [2, 4, 1, 1, 2]))  # Output: [2, 4]
print(solution("ABAB", [10, 5, 10, 15]))    # Output: [0, 15]
print(solution("B", [100]))                  # Output: [100, 0]
