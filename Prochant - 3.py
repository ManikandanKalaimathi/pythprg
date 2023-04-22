def robot_collisions(A):
    n = len(A)
    while True:
        left = []
        right = []
        for i in range(n):
            if A[i][1] == 0:
                left.append(i)
            else:
                right.append(i)
        if not left or not right:
            direction = A[0][1]
            return [(A[i][0], direction) for i in range(n)]
        
        i = 0
        j = 0
        del_indices = []
        while i < len(left) and j < len(right):
            if A[left[i]][0] > A[right[j]][0]:
                A[left[i]][0] -= A[right[j]][0]
                del_indices.append(right[j])
                j += 1
            elif A[left[i]][0] < A[right[j]][0]:
                A[right[j]][0] -= A[left[i]][0]
                del_indices.append(left[i])
                i += 1
            else:
                A[right[j]][0] = 0
                A[left[i]][0] = 0
                i += 1
                j += 1
                
        for index in sorted(del_indices, reverse=True):
            del A[index]         
            
        n = len(A)
        
n = int(input())
A = [list(map(int, input().split())) for i in range(n)]
result = robot_collisions(A)
for robot in result:
    print(robot[0], robot[1])
    
                                  