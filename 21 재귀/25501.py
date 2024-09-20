def recursion(s, f_s, l_s, count):
    count += 1
    if f_s >= l_s:
        return 1, count
    elif s[f_s] != s[l_s]:
        return 0, count
    else:
        return recursion(s, f_s + 1, l_s - 1, count)

def isPalindrome(s):
    count = 0
    return recursion(s, 0, len(s) - 1, count)

num = int(input())

for i in range(num):
    ans = list(isPalindrome(input()))
    print(ans[0], ans[1])