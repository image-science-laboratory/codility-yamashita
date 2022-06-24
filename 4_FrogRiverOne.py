def solution(X, A):
    # write your code in Python 3.6
    dic = {}
    for i in range(len(A)):
        if not A[i] in dic:
            dic[A[i]] = 1
        if i < X-1: continue
        if X == len(dic):
            return i
    return -1
