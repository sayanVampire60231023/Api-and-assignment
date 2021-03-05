
class Solution:
    def isValid(self, s: str) -> bool:
        opening = ['(','[','{']
        
        stk = []
        for bracket in s:
            if bracket in opening:
                stk.append(bracket)
            else:
                if bracket == ')' and len(stk) and stk[-1] == '(':
                    stk.pop()
                elif bracket == ']' and len(stk) and stk[-1] == '[':
                    stk.pop()
                elif bracket == '}' and len(stk) and stk[-1] == '{':
                    stk.pop()
                else:
                    return False
        
        return not len(stk)
