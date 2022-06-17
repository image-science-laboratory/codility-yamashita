# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    counter = [0]*N
    mx = 0
    mxx = 0
    for i in range(len(A)):
        if A[i] <= N:
            counter[A[i]-1] = max(counter[A[i]-1]+1, mx+1)
            mxx = max(mxx, counter[A[i]-1])
        else:
            mx = mxx
    for i in range(N):
        counter[i] = max(counter[i], mx)
    return counter