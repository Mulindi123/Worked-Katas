
def solution(S):
    char_count=0
    for char in set(S):
            x=S.count(char)
            print(x)
            if x%2 != 0:
                char_count+=1
            else:
                char_count==0
    return char_count  


solution("abcabcd")
#print(solution("abcaabc"))
# print(solution("propaganda"))