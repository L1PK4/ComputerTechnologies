from functools import reduce

n = int(input("Enter n: "))
print("Enter {0}x{0} matrix:".format(n))
a = [list(map(float, input().split(maxsplit=n))) for i in range(n)]
print("Sum = {0}\nMin = {1}".format(\
    list(map(sum, [i for i in a if (lambda x : reduce(lambda a, b: a and b >= 0, x, True))(i)])),\
    min(list(map(sum, [[a[i][i - k] for i in range(int((k + abs(k))/2),n + int((k - abs(k))/2))] for k in range(1 - n, n)])))
    ))