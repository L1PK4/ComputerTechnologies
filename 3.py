a = list(map(float, input("Input arr: ").split()))
def find(arr, step):
    for i in range(0 if step == 1 else -1, len(arr) if step == 1 else 0, 1 if step == 1 else -1):
        if arr[i] > 0:
            return i
print("Min = {0}\nSum = {1}\nNew arr = {2}".format(min(a), sum(a[find(a,1):find(a,-1)]), (list(filter(lambda x: x == 0., a)) + list(filter(lambda x: x != 0., a)))))
