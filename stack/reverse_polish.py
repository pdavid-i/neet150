class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = [int(tokens[0])]
        i = 1 
        while (i < len(tokens)):
            if (isOperand(tokens[i])):
                op2 = operands.pop()
                op1 = operands.pop()
                operands.append(eval(op1, op2, tokens[i]))
            else:
                operands.append(int(tokens[i]))
            i+=1
        return operands.pop()


def eval(op1: int, op2: int, operator:str) -> int:
    match operator:
        case "+":
            return op1+op2;
        case "-":
            return op1-op2;
        case "*":
            return op1*op2;
        case "/":
            return int(op1/op2);
    return None

def isOperand(char: str) -> bool:
    return char in ['+', '-', '/', '*']
