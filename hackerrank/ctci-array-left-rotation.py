a = [1,2,3,4,5]
n = 5
k = 1

def array_left_rotation(a, n, k):
    for item in a:
        print(item)

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
