# // 【程序7】
# // 题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
def countchars(str, startChar, endChar):
    startAscCode = min(ord(startChar), ord(endChar))
    endAscCode = max(ord(startChar), ord(endChar))
    result = 0
    for value in [chr(i) for i in range(startAscCode, endAscCode + 1)]:
        result += str.count(value)
    return result


str = input("请输入一个字符串： ")
print(f"您输入的字符串中数字的个数为:{countchars(str,'0','9')}");
print(
    f"您输入的字符串中英文字母的个数为:{countchars(str,'a','z')+countchars(str,'A','Z')}，小写字母个数为{countchars(str,'z','a')},大写字母个数为{countchars(str,'A','Z')}");
print(f"您输入的字符串中空格的个数为:{countchars(str,' ',' ')}");
print(
    f"您输入的字符串中其他字符的个数为:{len(str) - countchars(str,'0','9')-countchars(str,'a','z')-countchars(str,'A','Z')-countchars(str,' ',' ')}");
