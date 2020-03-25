class BoolExpr:
    precedence = 4
    pass

class Var(BoolExpr):
    precedence = 4

    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return str(self._x)

    def eval(self,d):
        return d[self._x]

class Const(BoolExpr):
    precedence = 4

    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return str(self._x)

    def eval(self,d):
        return self._x

class Not(BoolExpr):
    precedence = 3

    def __init__(self, x):
        super().__init__()
        self._x = x

    def __str__(self):
        return "~" + str(clean(self._x, self.precedence))

    def eval(self,d):
        return not self._x.eval(d)

class And(BoolExpr):
    precedence = 2

    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y

    def __str__(self):
        return str(clean(self._x, self.precedence)) + " /\\ " + str(clean(self._y, self.precedence))

    def eval(self,d):
        return self._x.eval(d) and self._y.eval(d)

class Or(BoolExpr):
    precedence = 1

    def __init__(self, x, y):
        super().__init__()
        self._x = x
        self._y = y

    def __str__(self):
        return str(clean(self._x, self.precedence)) + " \\/ " + str(clean(self._y, self.precedence))

    def eval(self,d):
        return self._x.eval(d) or self._y.eval(d)

def clean(Expr, precedence):
    if Expr.precedence < precedence:
        return "(" + str(Expr) + ")"
    else:
        return str(Expr)


# print(Var("x"))
# # x
# print(Const(False))
# # False
# print(And(Var("x"),Var("y")))
# # x /\ y
# print(Or(Var("x"),Var("y")))
# # x \/ y
# print(Not(Var("x")))
# # ~x
# print(And(Or(Var("x"),Var("y")),Not(Var("z"))))
# # (x \/ y) /\ ~z
# print(Or(Not(Const(True)),Var("x")))
# # ~True \/ x
# print(Not(And(Var("x"),Var("y"))))
# # ~(x /\ y)
# print(And(And(Var("x"),Var("y")),Var("z")))
# # x /\ y /\ z
# print(Or(Or(Var("x"),Var("y")),Var("z")))
# # x \/ y \/ z
# print(Not(Not(Var("x"))))
# # ~~x
# print(Or(Not(Var("x")),Var("x")))
# # ~x \/ x
