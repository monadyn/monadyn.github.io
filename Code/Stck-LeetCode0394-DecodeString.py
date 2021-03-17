s = "3[a]2[bc]"#, return "aaabcbc".
s = "3[a2[c]]"#, return "accaccacc".
s = "2[abc]3[cd]ef"#, return "abcabccdcdcdef".
def decodeString(s):
    #遇到’[‘就把之前的字符串进行进栈操作。遇到’]'进行出栈操作。
    #curstring = prestring + prenum * curstring，prestring是前面的字符串，prenum * curstring是这一步骤结束之后的字符串，所以是前面的字符串+现在的字符串得到目前已有的字符串。
        curnum = 0
        curstring = ''
        stack = []
        for char in s:
            if char == '[':
                stack.append(curstring) #先放prestring
                stack.append(curnum)
                curstring = ''
                curnum = 0
            elif char == ']':
                prenum = stack.pop()
                prestring = stack.pop()
                curstring = prestring + prenum * curstring
            elif char.isdigit():
                #连续数字
                curnum = curnum * 10 + int(char)
            else:
                curstring += char
        return curstring
print(decodeString(s))
