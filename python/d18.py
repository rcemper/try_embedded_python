from collections import deque
import re

class Expression:
    def __init__(self, subtree=None, parent=None):
        self.addleft(None)
        self.addright(subtree)
        self.parent = parent

    def addleft(self, subtree):
        self.left = subtree
        if subtree:
            subtree.parent = self

    def addright(self, subtree):
        self.right = subtree
        if subtree:
            subtree.parent = self

    def value(self):
        return self.right.value()  # Hacky way to make parsing easier

    def replace(self, old, new):
        """
        Replaces child old with new and returns the old.
        Does nothing if old is not a child of this node.
        """
        if self.left == old:
            tmp = self.left
            self.addleft(new)
            return tmp
        if self.right == old:
            tmp = self.right
            self.addright(new)
            return tmp

    def tostring(self):
        return f'[{self.right.tostring()}]'


class Num:
    def __init__(self, n):
        self.right = n

    def value(self):
        return self.right

    def tostring(self):
        return str(self.right)


class Operator(Expression):
    def __init__(self, op, left=None, right=None):
        super().__init__(self)
        self.operator = op
        self.addleft(left)
        self.addright(right)

    def value(self):
        if self.operator == '+':
            return self.left.value() + self.right.value()
        elif self.operator == '*':
            return self.left.value() * self.right.value()
        raise ArithmeticError(f'Unknown operator: {self.operator}')

    def tostring(self):
        return f'({self.left.tostring()} {self.operator} {self.right.tostring()})'


def generate_tree(tokens):
    """
    Param tokens: a deque of tokens (either a number, '+', '*', '(', or ')')
    """
    expression = Expression()
    while len(tokens) > 0:
        token = tokens.popleft()
        if type(token) is int:
            # Assumes that expression is an Operator or Expression
            expression.addright(Num(token))
        elif token in ('+', '*'):
            expression = Operator(token, left=expression)
        elif token == '(':
            # Assumes that expression is an Operator or Expression, generates a subexpression
            expression.addright(generate_tree(tokens))
        elif token == ')':
            # Closing subexpression, return result to caller
            return expression
    # Finished parsing
    return expression


def set_precedence(subtree, operator):
    #        P            P
    #       /            /
    #      +      =>    *
    #     / \          / \
    #    *   C        A   +
    #   / \              / \
    #  A   B            B   C
    #

    # First process subtrees, this way we can use recursion to replace nodes
    if subtree.left and isinstance(subtree.left, Expression):
        subtree.addleft(set_precedence(subtree.left, operator))
    if subtree.right and isinstance(subtree.right, Expression):
        subtree.addright(set_precedence(subtree.right, operator))

    # Change the precedence by sinking operators with higher precedence to the bottom
    if type(subtree) is Operator and subtree.operator == operator and type(subtree.left) is Operator and subtree.left.operator != operator:
        left = subtree.left
        right = left.right
        subtree.addleft(left.replace(right, subtree))
        return left
    else:
        return subtree

tokenise_pattern = re.compile(r'(\d+|[()*+])')

with open('../stream/input18.txt', 'r') as f:
    total1 = 0
    total2 = 0
    for line in f:
        tokens = deque(int(t) if t.isnumeric() else t for t in map(lambda s: s.groups()[0], tokenise_pattern.finditer(line)))
        expr = generate_tree(tokens)
        total1 += expr.value()
        expr = set_precedence(expr, '+')
        total2 += expr.value()
 #   print(f'Part 1: {total1}')
 #   print(f'Part 2: {total2}')

def p1():
    return str(total1)
def p2():
    return str(total2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            