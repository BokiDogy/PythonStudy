# //    题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
#     ////这是一个菲波拉契数列问题
#     //public class lianxi01 {
#     //public static void main(String[] args) {
#     //System.out.println("第1个月的兔子对数:    1");
#     //System.out.println("第2个月的兔子对数:    1");
#     //int f1 = 1, f2 = 1, f, M=24;
#     //     for(int i=3; i<=M; i++) {
#     //      f = f2;
#     //      f2 = f1 + f2;
#     //      f1 = f;
#     //      System.out.println("第" + i +"个月的兔子对数: "+f2);
#     //         }
#     //}
#     //}
def fbnq(n, res1, res2):
    if n == 1:
        return res1
    else:
        return fbnq(n - 1, res1 + res2, res1)


n = int(input("所求月份n:"))
for i in range(1, n + 1):
    print(f"第{i}个月兔子对数为:{fbnq(i,1,0)}")
