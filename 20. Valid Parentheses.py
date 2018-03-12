class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    a = stack.pop(-1)
                    if (a == '(' and i == ')') or (a == '{' and i == '}') or (a == '[' and i == ']'):
                        continue                ##此处不能return，因为for循环还没有结束
                    else:
                        return False
        if len(stack) != 0:
            return False
        else:
            return True
