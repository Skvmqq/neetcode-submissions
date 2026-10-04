from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        operators = ['+', '-', '*', '/']
        stack = deque()
        for token in tokens:
            if token not in operators:
                token = int(token)
                stack.appendleft(token)
            else:
                
                a= stack.popleft()
                b =stack.popleft()
                if token == "+":
                    result = a +b 
                    stack.appendleft(result)

                elif token == "*":
                    result = int(a*b) 
                    stack.appendleft(result)
                elif token == "-":
                    result = b -a 
                    stack.appendleft(result)
                elif token == "/":
                    result = int(b/ a) 
                    stack.appendleft(result)
    
        return stack.popleft()





            
        
        