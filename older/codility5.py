
def solution(S):
#         len(word1) = len(word2)=len(word(len(s)-1)). All the words have the same length
#         if word1[i] == word2[i]
#         S = ["abc", "dbc", "dcf", "zcf", "cdf"] // Possible array
#         Accessing first element of S = S[0]
#         Accessing the ith element of S = S[i]
#         Accessing the 1st element of the string of the ith element of S = S[i][1]
#         => if S[i][a] == S[j][a] we found our pair

    for i in range(len(S[0])):  #range of first string since they have same length. Get index position letters of the strings
        for j in range(len(S)):  # range of the entire array. Get the index position of each word
            for k in range(j+1, len(S)): # get the index position of the next word 
                if S[j][i] == S[k][i]:
                    return [j,k,i]

    return []

# def solution(S):
#     char_index_map = {}  # A dictionary to store character indices
    
#     for i in range(len(S[0])):
#         char_index_map.clear()  # Clear the map for each new index
        
#         for j in range(len(S)):
#             char = S[j][i]
            
#             if char in char_index_map:
#                 return [char_index_map[char], j, i]
#             else:
#                 char_index_map[char] = j
    
#     return []


print(solution(["abc", "dbc", "cdf"]))
# print(solution(["abc", "bca", "dbe"]))
#print(solution( ["zzzz", "ferz", "zdsr", "fgtd"])) # zzzz/ferz, zzzz/zdsr, ferz/fgtd
print(solution(["gr", "sd", "rg"]))
#print(solution( ["bdafg", "ceagi"]))