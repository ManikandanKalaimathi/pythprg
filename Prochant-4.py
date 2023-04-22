def solve(N, A):
    stack = []
    for i in range(N):
        health, direction = A[i]
        while stack and stack[-1][1] != direction:
            other_health, other_direction = stack.pop()
            if health > other_health:
                health -= other_health
            elif health == other_health:
                break
            # otherwise, the current robot is knocked out and
            # we continue the loop to check against the next robot
        else:
            # no robot in the stack is moving in the opposite direction,
            # so we simply push the current robot onto the stack
            stack.append((health, direction))

    # pop the remaining robots from the stack and add them to the result list
    result = []
    while stack:
        health, direction = stack.pop()
        result.append((health, direction))

    # reverse the result list to get the correct order
    result.reverse()
    return result