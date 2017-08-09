def partition(a):
    pivot = a[0]
    left, right = 0, len(a) - 1
    while left != right:
        while right != left and a[right] > pivot:
            right -= 1
        a[left], a[right] = a[right], a[left]
        while left != right and a[left] <= pivot:
            left += 1
        a[left], a[right] = a[right], a[left]

def main():
    n = int(raw_input().strip())
    a = map(int, raw_input().strip().split())
    partition(a)
    print ' '.join(map(str, a))

if __name__ == '__main__':
    main()
