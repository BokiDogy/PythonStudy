# // 【程序2】
# // 题目：判断101 - 200
# 之间有多少个素数，并输出所有素数。
# // 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除， 则表明此数不是素数，反之是素数。
# // public
#
#
# class lianxi02
#     // {
#        // public
#     static
#     void
#     main(String[]
#     args)
#     // {
#        // int
#     count = 0;
#     // for (int i = 101; i < 200; i += 2)
#            // {
#            // boolean b = false;
#     // for (int j = 2; j <= Math.sqrt(i); j++)
#     // {
#     // if (i % j == 0) {b = false;
#
#
# break;}
# // else {b = true;}
# //}
# // if (b == true) {count++; System.out.println(i);}
# //}
# // System.out.println("素数个数是: " + count);
# //}
# //}
import math as M

x = int(input("m: "))
y = int(input("n: "))
z = 1
for n in range(x, y + 1):
    isZhi = True
    for i in range(2, M.floor(M.sqrt(n) + 1)):
        if n % i == 0:
            isZhi = False
            break
    if isZhi:
        print(f"{x}-{y}间：第{z}项质数是{n}")
        z += 1
