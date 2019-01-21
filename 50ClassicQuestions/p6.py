# // {【程序6】
# // 题目：输入两个正整数m和n，求其最大公约数和最小公倍数。
# // / ** 在循环中，只要除数不等于0，用较大数除以较小的数，将小的一个数作为下一轮循环的大数，取得的余数作为下一轮循环的较小的数，如此循环直到较小的数的值为0，返回较大的数，此数即为最大公约数，最小公倍数为两数之积除以最大公约数。 * /
m = int(input("m: "))
n = int(input("n: "))
if n % m == 0 or m % n == 0:
    i = n if (m > n) else m
else:
    k = i = (n / 2) if (m > n) else (m / 2)
    j = 1
    while j <= k and ((n % i != 0) or (m % i != 0)):
        j += 1
        if ((n / j) if (m > n) else (m / j)) % 1 != 0:
            continue
        else:
            i = (n / j) if (m > n) else (m / j)
    if j > k:
        i = 1

print(f"您输入的两个数字{m}、{n}的最大公约数为：{int(i)}")
print(f"您输入的两个数字{m}、{n}的最小公倍数为：{int(m * n / i)}")
