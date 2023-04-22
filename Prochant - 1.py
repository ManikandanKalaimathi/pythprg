def findSum (N, q, queries):
    mod=10**9+7
    matrix=[[0]*N for _ in range(N)]

    
    for query in queries:
        if query[0]==1:
            rid,val=query[1]-1,query[2]
            for j in range(N):
                matrix[rid][j]=val%mod
            
        else:
            cid,val=query[1]-1,query[2]
            for i in range(N):
                matrix[i][cid]=val%mod
        
    t=0
    for i in range(N):
        for j in range(N):
            t+=matrix[i][j]
    return t%mod

    return ans


    pass

t = int(input())

for i in range(t):
    N = int(input())
    q = int(input()) 
    queries = []
    for j in range(q):
        query = list(map(int, input().split()))
        queries.append(query)
    result = findSum(N, q, queries)
    print(result)
                
                 