from re import L


def printAllPossibleCombinations(arr, n, r):
    output = []
    def recurse(arr, temp):
        if len(temp) == r:
            output.append(temp)
            return
        for i in range(len(arr)):
            recurse(arr[i+1:], temp + [arr[i]])
    recurse(arr, [])
    print(output)


arr = [1,2,3,4,5,6]
n = len(arr)
r = 3
printAllPossibleCombinations(arr, n, r)