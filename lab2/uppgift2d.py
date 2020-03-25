class BoolExpr:
    precedence = 4
    def printTruthTable(self):
        variables = extractVars(str(self))
        firstRow = " | ".join(variables) + " | " + str(self)
        nLines, lines = 2**(len(variables)), []
        for i in range(nLines):
            lines.append({})
        for j in range(len(variables)):
            switch, sValue = nLines//(2**(j+1)), False
            for i in range(nLines):
                if i % switch == 0:
                    sValue = not sValue
                lines[i][str(variables[j])] = sValue
        print(firstRow + "\n" + "-" * len(firstRow))
        for e in lines:
            line = []
            for v in variables:
                line.append(convertTo01(e[v]))
            print(" | ".join(line) + " | " + convertTo01(self.eval(e)))
        print("")

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

def convertTo01(bool):
    if bool == True:
        return "1"
    return "0"

def extractVars(exprStr):
    exprStr = exprStr.replace('(','')
    exprStr = exprStr.replace(')','')
    exprStr = exprStr.replace('\\/','')
    exprStr = exprStr.replace('/\\','')
    exprStr = exprStr.replace('~','')
    exprStr = exprStr.replace('False','')
    exprStr = exprStr.replace('True','')
    return exprStr.split()


(Not(Var("x"))).printTruthTable()
# x | ~x
# ------
# 1 | 0
# 0 | 1
#
(Or(Var("x"),Const(False))).printTruthTable()
# x | x \/ False
# --------------
# 1 | 1
# 0 | 0
#
(And(Var("x"),Var("y"))).printTruthTable()
# x | y | x /\ y
# --------------
# 1 | 1 | 1
# 1 | 0 | 0
# 0 | 1 | 0
# 0 | 0 | 0
#
(And(Or(Var("x"),Var("y")),Var("z"))).printTruthTable()
# x | y | z | (x \/ y) /\ z
# -------------------------
# 1 | 1 | 1 | 1
# 1 | 1 | 0 | 0
# 1 | 0 | 1 | 1
# 1 | 0 | 0 | 0
# 0 | 1 | 1 | 1
# 0 | 1 | 0 | 0
# 0 | 0 | 1 | 0
# 0 | 0 | 0 | 0
#
(And(Or(Var("x"),Var("y")),Or(Not(Var("z")),Var("w")))).printTruthTable()
# x | y | z | w | (x \/ y) /\ (~z \/ w)
# -------------------------------------
# 1 | 1 | 1 | 1 | 1
# 1 | 1 | 1 | 0 | 0
# 1 | 1 | 0 | 1 | 1
# 1 | 1 | 0 | 0 | 1
# 1 | 0 | 1 | 1 | 1
# 1 | 0 | 1 | 0 | 0
# 1 | 0 | 0 | 1 | 1
# 1 | 0 | 0 | 0 | 1
# 0 | 1 | 1 | 1 | 1
# 0 | 1 | 1 | 0 | 0
# 0 | 1 | 0 | 1 | 1
# 0 | 1 | 0 | 0 | 1
# 0 | 0 | 1 | 1 | 0
# 0 | 0 | 1 | 0 | 0
# 0 | 0 | 0 | 1 | 0
# 0 | 0 | 0 | 0 | 0
