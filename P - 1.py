def solve (N, A):
    r = [(h,d) for h,d in A]
    i = 0
    while i<len(r)-1:
        if r[i][1]==1 and r[i+1][1]==0:
            if r[i][0]>r[i+1][0]:
                r[i]=(r[i][0]-r[i+1][0],1)
                del r[i+1]
                i = max(i-1,0)
            elif r[i][0]<r[i+1][0]:
                r[i+1]=(r[i+1][0]-r[i][0],0)
                del r[i]
                i = max(i-1,0)
            else:
                del r[i:i+2]
                i = max(i-1,0)
        else:
            i+=1
    return r
    pass

N = input()
A = []
for _ in xrange(N):
    A.append(map(int, raw_input().split()))
    
out_ = solve(N, A)
for i_out_ in out_:
    print ' '.join(map(str, i_out_))                          