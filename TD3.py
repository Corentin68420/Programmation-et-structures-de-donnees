
import unittest

class Tree:

    def __init__(self,label, *children):
        self._label = label
        self._children = children



    def label(self):
        return str(self._label)

    def children(self):
        return self._children

    def child(self,i):
        return self._children[i-1]

    def nb_children(self):
        return len(self._children)

    def is_leaf(self):
        if self.nb_children == 0:
            return True
        return False



    def depth(self):
        if self.is_leaf():
            return 0
        return 1 + max([child.depth() for child in self.children()])

# Children me renvoie un tuple dont le dernier élément est vide ce qui pose problème pour le max, je n'arrive pas à enlever cet élément.


    def __eq__(self, other):

        if self.label() != other.label():
            return False
        if len(self.children()) != len(other.children()):
            return False
        for self_child, other_child in zip(self.children(), other.children()):
            if self_child != other_child:
                return False
        return True


    def __str__(self):
        if self.is_leaf():
            return self._label()
        string = self._label() + '('
        for child in self.children():
            string += child.__str__() + ','
        string = string.rstrip(',') + ")"
        return string

    def deriv(self, var: str) -> 'Tree':
        if self.is_leaf():
            if self._label() == var:
                return Tree(1)
            else:
                return Tree(0)
        else:
            if self._label() == '+':
                return Tree('+', *[child.deriv(var) for child in self.children()])
            elif self.label() == '*':
                if any(child.label() == var for child in self.children()):

                    L = []
                    T = []
                    i = 0
                    for child in self.children():
                        for j in range(len(self.children())):
                            if j == i:
                                T.append(self.child(i).deriv(var))
                            else:
                                T.append(self.child(i))
                        L.append(Tree('*', *T))
                        T = []
                        i+=1
                    print(L)
                    return Tree('+', *L)
                else:
                    return Tree(0)
            else:
                return "error"











tree = Tree(2,Tree(3))
tree.depth()
#print(tree.label())
#print(tree.children())
#print(tree.child(1))
#print(tree.nb_children())
#print(tree.is_leaf())
