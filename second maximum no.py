if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ans = list(set(arr))
    ans.sort()
    print(ans[-2])
