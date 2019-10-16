def miniMaxSum(arr):
    a=sum(arr)
    minValue=a-max(arr)
    maxValue=a-min(arr)
    print(minValue,maxValue,end="")
    
    
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
