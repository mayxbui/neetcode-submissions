class Solution:
    def isValid(self, s: str) -> bool:
        valid = {")":"(","]":"[","}":"{"}
        stack = []

        for i in s:
            if i in valid:
                if len(stack)!=0:
                    top = stack.pop()
                else:
                    return False
                if valid[i]!=top:
                        return False
            else:
                stack.append(i)
        return len(stack)==0

