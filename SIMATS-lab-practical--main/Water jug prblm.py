from math import gcd

def water_jug_problem(m, n, d):
    # Check if solution is possible
    if d > max(m, n):
        return "Not possible"
    if d % gcd(m, n) != 0:
        return "Not possible"

    # Helper function to simulate pouring
    def pour(fromCap, toCap, target):
        fromJug, toJug = fromCap, 0
        steps = [(fromJug, toJug)]

        while (fromJug != target) and (toJug != target):
            # Find the maximum amount that can be poured
            temp = min(fromJug, toCap - toJug)

            # Pour "temp" from fromJug to toJug
            toJug += temp
            fromJug -= temp
            steps.append((fromJug, toJug))

            # If one jug has target liters
            if fromJug == target or toJug == target:
                break

            # If fromJug becomes empty, fill it
            if fromJug == 0:
                fromJug = fromCap
                steps.append((fromJug, toJug))

            # If toJug becomes full, empty it
            if toJug == toCap:
                toJug = 0
                steps.append((fromJug, toJug))

        return steps

    # Try both ways: start with jug m or jug n
    steps1 = pour(m, n, d)
    steps2 = pour(n, m, d)

    # Return the one with fewer steps
    return steps1 if len(steps1) <= len(steps2) else steps2


# Example usage
m, n, d = 4, 3, 2
solution = water_jug_problem(m, n, d)

print("Steps to solve:")
for step in solution:
    print(step)
