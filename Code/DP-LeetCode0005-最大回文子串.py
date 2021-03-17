def longestPalindrome(s):
    #直观的动态规划解法，我们首先初始化一字母和二字母的回文，然后找到所有三字母回文，并依此类推…
        n = len(s)
        maxl, start = 0, 0
        for i in range(n):
            print(i, start, maxl)
            print('\t', i-maxl-1, i+1, s[i-maxl-1:i+1])
            #回看2个
            if i - maxl >= 1 and s[i-maxl-1:i+1] == s[i-maxl-1:i+1][::-1]:
                start = i - maxl - 1
                maxl += 2 #增加2个
                print('\t\t', start, maxl)
                continue
            #回看1个
            print('\t', i-maxl, i+1, s[i-maxl:i+1])
            if i - maxl >= 0 and s[i-maxl:i+1] == s[i-maxl:i+1][::-1]:
                start = i - maxl
                maxl += 1 #增加1个
                print('\t\t', start, maxl)
        return s[start: start + maxl]

inStr = 'babaieirdabba'
print(len(inStr), inStr)
print(longestPalindrome(inStr))

def longestPalindrome_(s):
        longest_str = ''
        n = [len(s) - 1]
        print(n)

        #why?
        for diff in range(1, len(s)):
            n.append(n[0] + diff)
            n.append(n[0] - diff)
        print(n)

        for i in n:
            if (min(i + 1, 2 * len(s) - 1 - i) <= len(longest_str)):
                print('b:', i + 1, 2 * len(s) - 1 - i, longest_str)
                break

            if i % 2 == 0:
                left, right = (i // 2) - 1, (i // 2) + 1
            else:
                left, right = i // 2, (i // 2) + 1
            
            #判断回文
            print(i, left, right, s[left:right+1])
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            print(left, right)

            if right - left - 1 > len(longest_str):
                longest_str = s[left + 1: right]

        return longest_str

