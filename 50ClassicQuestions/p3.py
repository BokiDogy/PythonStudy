# //    题目：打印出所有的 "水仙花数 "，所谓 "水仙花数 "是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个 "水仙花数 "，因为153=1的三次方＋5的三次方＋3的三次方。
# //public class lianxi03
# //    {
# //        public static void main(String[] args)
# //        {
# //            int b1, b2, b3;
# //            for (int m = 101; m < 1000; m++)
# //            {
# //                b3 = m / 100;
# //                b2 = m % 100 / 10;
# //                b1 = m % 10;
# //                if ((b3 * b3 * b3 + b2 * b2 * b2 + b1 * b1 * b1) == m)
# //                {
# //                    System.out.println(m + "是一个水仙花数");
# //                }
# //            }
# //        }
# //    }
count = 0
for number in range(100, 1000):
    if number == ((int(number / 100)) ** 3) + ((int(number / 10) % 10) ** 3) + ((number % 10) ** 3):
        count += 1
        print(f"第{count}个水仙花数为：{number}")
