def solution(A):
    # write your code in Python 3.6
    dic = {}
    for a in A:
        dic[a] = 1

    for i in range(1, len(A) + 1):
        if not i in dic:
            return 0
    return 1
