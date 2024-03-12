# Нехай на кожну сходинку можна стати з попередньої або переступивши через одну. Визначте, скількома способами можна піднятися на задану сходинку.
#
def climbStairs(n):
    if n == 1 or n == 0:
        return 1
    if n == 2:
        return 2

    ways = [0] * (n + 1)
    ways[0], ways[1], ways[2] = 1, 1, 2

    for i in range(3, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]

    return ways[n]


n = 5
print(climbStairs(n))
