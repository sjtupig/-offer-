# -*- coding:utf-8 -*-
#以空间换时间
class Solution1:
    def LeftRotateString(self, s, n):
        # write code here
        
        return s[n:]+s[:n]


#这题还可以用字符串翻转的方法来做      !!!重点，字符串翻转
# -*- coding:utf-8 -*-
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        arrays = list(s)
        def reverse(a):
            l, r = 0, len(a)-1
            while l < r:
                a[l],a[r] = a[r],a[l]
                l+=1
                r-=1
            return a 
        
        arrays[:n] = reverse(arrays[:n])  #切片操作得到的结果，不是对象的引用
        #print arrays
        arrays[n:] = reverse(arrays[n:])
        #print arrays
        arrays = reverse(arrays)
        #print arrays
        
        return ''.join(arrays)

sol = Solution()
print sol.LeftRotateString('1234', 2)