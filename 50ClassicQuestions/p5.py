# //    【程序5】
# //题目：利用条件运算符的嵌套来完成此题：学习成绩> =90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
# //import java.util.*;
# //    public class lianxi05
# //    {
# //        public static void main(String[] args)
# //        {
# //            int x;
# //            char grade;
# //            Scanner s = new Scanner(System.in);
# //            System.out.print("请输入一个成绩: ");
# //            x = s.nextInt();
# //            grade = x >= 90 ? 'A'
# //                  : x >= 60 ? 'B'
# //                  : 'C';
# //            System.out.println("等级为：" + grade);
#
# //        }
# //    }
score = int(input("学生的分数n=: "))
result = ""
if score >= 0 and score <= 100:
    result = "A" if (score >= 90) else ("C" if (score < 60) else "B")
    print(f"该学生的成绩为：{result}")
else:
    print("您输入的分数无效")
