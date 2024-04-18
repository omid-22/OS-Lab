# First-Fit algorithm


def firstFit(blockSize, m, processSize, n):

    alloc = [-1] * n

    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:

                alloc[i] = j

                blockSize[j] = blockSize[j] - processSize[i]

                break

    print(" Process No.  Process Size	 Block Size   Block No.")
    for i in range(n):
        print(
            " ", i + 1, "		 ", processSize[i], "		 ", blockSize[i], "         ", end=""
        )
        if alloc[i] != -1:
            print(alloc[i] + 1)
        else:
            print("Not Allocated")

    print("remaining blocksizes are: ", blockSize)


blockSize = []
m = int(input("Enter number of blocks :"))
for i in range(m):
    newblock = int(input())
    blockSize.append(newblock)


processSize = []
n = int(input("Enter number of processes :"))
for i in range(n):
    newprocess = int(input())
    processSize.append(newprocess)


firstFit(blockSize, m, processSize, n)
