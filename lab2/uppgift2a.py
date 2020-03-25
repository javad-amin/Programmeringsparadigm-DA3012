class BoolExpr:
    pass

class Var(BoolExpr):
    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return str(self._x)

    def eval(self,d):
        return d[self._x]

class Const(BoolExpr):
    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return str(self._x)

    def eval(self,d):
        return self._x

class Not(BoolExpr):
    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return "~(" + str(self._x) + ")"

    def eval(self,d):
        return not self._x.eval(d)

class And(BoolExpr):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y

    def __str__(self):
        return "(" + str(self._x) + ") /\\ (" + str(self._y) + ")"

    def eval(self,d):
        return self._x.eval(d) and self._y.eval(d)

class Or(BoolExpr):
    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y

    def __str__(self):
        return "(" + str(self._x) + ") \\/ (" + str(self._y) + ")"

    def eval(self,d):
        return self._x.eval(d) or self._y.eval(d)


# print(Var("x"))
# #x
# print(Const(False))
# #False
# print(And(Var("x"),Var("y")))
# #(x) /\ (y)
# print(Or(Var("x"),Var("y")))
# #(x) \/ (y)
# print(Not(Var("x")))
# #~(x)
# print(And(Or(Var("x"),Var("y")),Not(Var("z"))))
# #((x) \/ (y)) /\ (~(z))
# print(Or(Not(Const(True)),Var("x")))
# #(~(True)) \/ (x)
# print(Not(And(Var("x"),Var("y"))))
# #~((x) /\ (y))
# print(And(And(Var("x"),Var("y")),Var("z")))
# #((x) /\ (y)) /\ (z)
# print(Or(Or(Var("x"),Var("y")),Var("z")))
# #((x) \/ (y)) \/ (z)
# print(Not(Not(Var("x"))))
# #~(~(x))
# print(Or(Not(Var("x")),Var("x")))
# #(~(x)) \/ (x)
# d1 = {"x" : False }
# print((Or(Not(Var("x")),Var("x"))).eval(d1))
# #True
# d2 = {"x" : False , "y" : True , "z" : True }
# print((And(And(Var("x"),Var("y")),Var("z"))).eval(d2))
# #False
# d3 = {"x" : False , "y" : True , "z" : False }
# print((And(Or(Var("x"),Var("y")),Not(Var("z")))).eval(d3))
# #True
# print((Var("x")).eval(d3))
# #False
# print((Const(False)).eval(d3))
# #False
