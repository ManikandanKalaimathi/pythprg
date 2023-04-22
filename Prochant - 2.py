import sys
n = int(input())
robots = []
for i in range(n):
    health, direction = map(int, input().split())
    robots.append((health, direction))
i = 0
while i < len(robots) - 1:
    j = i + 1
    while j < len(robots):
        if robots[i][1] == 1 and robots[j][1] == 0:
            if robots[i][0] > robots[j][0]:
                robots[i] = (robots[i][0] - robots[j][0], robots[i][1])
                del robots[j]
                j -= 1
            elif robots[j][0] > robots[i][0]:
                robots[j] = (robots[j][0] - robots[i][0], robots[j][1])
                del robots[i]
                i -= 1
                break
            else:
                del robots[i]
                del robots[j-1]
                i -= 1
                break
        elif robots[i][1] == 0 and robots[j][1] == 1:
            if robots[i][0] < robots[j][0]:
                robots[j] = (robots[j][0] - robots[i][0], robots[j][1])
                del robots[i]
                i -= 1
                break
            elif robots[j][0] < robots[i][0]:
                robots[i] = (robots[i][0] - robots[j][0], robots[i][1])
                del robots[j]
                j -= 1
            else:
                del robots[i]
                del robots[j-1]
                i -= 1
                break
        j += 1
    i += 1

for robot in robots:
    print(robot[0], robot[1])
sys.exit()   