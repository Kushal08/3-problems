import sys

def long_subsequence(input_array):
    n = len(input_array)

    long_subsequence = [1]*n

    prev = [0]*n
    for i in range(0, n):
        prev[i] = i

    for i in range (1 , n):
        for j in range(0 , i):
            if input_array[i] > input_array[j] and long_subsequence[i]< long_subsequence[j] + 1:
                long_subsequence[i] = long_subsequence[j]+1
                prev[i] = j

 
    maximum = 0
    index = 0

    for i in range(n):
        if maximum < long_subsequence[i]:
            maximum = long_subsequence[i]
            index = i

    seq = [input_array[index]]
    while index != prev[index]:
        index = prev[index]
        seq.append(input_array[index])

    return (reversed(seq))

line1 =sys.stdin.readline()
N = line1[0]
line =sys.stdin.readline()
line = line.split(' ')

input_array = line[0:len(line)]

ans = long_subsequence(input_array)
print " ".join(str(x) for x in ans)   


