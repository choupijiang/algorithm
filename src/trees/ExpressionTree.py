# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
 author : choupijiang
"""

from LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    """
    An arithmetic expression tree.
    """

    def __init__(self, token, left=None, right=None):
        """
        Create an expression tree.
        In a single parameter form,token should be a leaf value, and the expression tree will have have that value at an isolated node.

        In a three-parameter version, token should be an operator and left and right should be existing ExpressionTree instances that become the operands for the binary operator.
        :param token:
        :param left:
        :param right:
        :return:
        """
        super(ExpressionTree, self).__init__()
        if not isinstance(token, str):
            raise TypeError("Token must be a string.")
        self._add_root(token)
        if left is not None:
            if token not in '+-*X/':
                raise ValueError("token must be valid operation")
            self._attach(self.root(), left, right)

    def _parenthesize_recur(self, p, result):
        """
        Append piecewise representation of p's subtree to resulting list.
        :param p:
        :param result:
        :return:
        """
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append("(")
            self._parenthesize_recur(self.left(p), result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p), result)
            result.append(")")


    def __str__(self):
        """
        Return string representation of the expression.
        :return:
        """
        pieces = []
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)


    def _evaluate_recur(self, p):
        """
        Return the numeric result of subtree rooted at p.
        :param p:
        :return:
        """
        if self.is_leaf(p):
            return float(p.element())
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == "+": return left_val + right_val
            elif op == "-": return left_val - right_val
            elif op == "/": return  left_val / right_val
            else: return left_val * right_val

    def evaluate(self):
        """
        Return the numeric result of the expression.
        :return:
        """
        return self._evaluate_recur(self.root())


def build_expression_tree(tokens):
    """
    Return an ExpressionTree based upen by a tokenized expression.
    :param tokens:
    :return:
    """
    S = []
    for t in tokens:
        if t in '+-X*/':
            S.append(t)
        elif t not in '()':
            S.append(ExpressionTree(t))
        elif t ==")":
            right = S.pop()
            op = S.pop()
            left = S.pop
            S.append(ExpressionTree(op, left, right))
    return S.pop()

if __name__ == "__main__":
    et = build_expression_tree("(((3+1)*4)/((9-5)+2))")
    print et
