class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        ans = 10**10
        for i in range(len(A)-M+1):
            ans = min(ans, A[i+M-1] - A[i])
        return ans