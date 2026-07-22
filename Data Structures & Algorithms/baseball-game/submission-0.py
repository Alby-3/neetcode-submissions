class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        num = 0
        for i in range(len(operations)):
            if operations[i] == "+":
                num =  stack[-1]+stack[-2]
                stack.append(num)
                num = 0
            elif operations[i] == "C":
                stack.pop()
            elif operations[i]=="D":
                stack.append(stack[-1]* 2)
            else:
                stack.append(int(operations[i]))

        return sum(stack)
