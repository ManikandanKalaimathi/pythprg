n = int(input())

for i in range(1, n+1):
    for j in range(1, n+1):
        if j == i or j == n-i+1:
            print(n-j+1, end='')
        else:
            print(' ', end='')
    print()            