
def countWays(n):
    if n==1:
        return 1
    steps = [0 for i in range(n+1)]
    steps[0] = 1
    steps[1] = 1 
    for i in range(2, n+1):
        if i-1 >= 0:
            steps[i] +=  steps[i-1] 
        if i-2 >= 0:
            steps[i] +=  steps[i-2]
        if i-3 >= 0:
            steps[i] += steps[i-3]
    return steps[n]

def countWaysNoMem(n):
    t0 = 0
    t1 = 0
    t2 = 1
    for i in range(n):
        t2 = t0 + t1 + t2
        t1 = t2 - t0 - t1
        t0 = t2 - t1 - t0
    return t2

def main():
    for i in range(1, 10):
        print countWays(i)
        print "No mem: ", countWaysNoMem(i)
    print countWays(10)

if __name__ == '__main__':
    main()
