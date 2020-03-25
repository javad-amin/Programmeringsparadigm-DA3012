import java.util.Map;
import java.util.HashMap;

abstract class BoolExpr {
    int precedence = 4;
    abstract public Boolean eval(Map d);
}

class Var extends BoolExpr {
    String x;

    public Var(String x) {
        super();
        this.x = x;
        this.precedence = 4;
    }

    public String toString() {
        return this.x;
    }

    public Boolean eval(Map d) {
        return (Boolean)d.get(this.x);
    }
}

class Const extends BoolExpr {
    Boolean x;

    public Const(Boolean x) {
        super();
        this.x = x;
        this.precedence = 4;
    }

    public String toString() {
        return String.valueOf(this.x);
    }

    public Boolean eval(Map d) {
        return this.x;
    }
}

class Not extends BoolExpr {
    BoolExpr x;

    public Not(BoolExpr x) {
        super();
        this.x = x;
        this.precedence = 3;
    }

    public String toString() {
      if (this.x.precedence < this.precedence) {
            return "~(" + String.valueOf(this.x) + ")";
        } else {
            return "~" + String.valueOf(this.x);
        }
    }

    public Boolean eval(Map d) {
        return !this.x.eval(d);
    }
}

class And extends BoolExpr {
    BoolExpr x;
    BoolExpr y;

    public And(BoolExpr x, BoolExpr y) {
        super();
        this.x = x;
        this.y = y;
        this.precedence = 2;
    }

    public String toString() {
        String result = "";
        if (this.x.precedence < precedence) {
            result = result + "(" + String.valueOf(this.x) + ") /\\ ";
        } else {
            result = result + String.valueOf(this.x) + " /\\ ";
        }
        if (this.y.precedence < precedence) {
            result = result + "(" + String.valueOf(this.x) + ")";
        } else {
            result = result + String.valueOf(this.y);
        }
        return result;
    }

    public Boolean eval(Map d) {
        return this.x.eval(d) && this.y.eval(d);
    }
}

class Or extends BoolExpr {
    BoolExpr x;
    BoolExpr y;

    public Or(BoolExpr x, BoolExpr y) {
        super();
        this.x = x;
        this.y = y;
        this.precedence = 1;
    }

    public String toString() {
        String result = "";
        if (this.x.precedence < precedence) {
            result = result + "(" + String.valueOf(this.x) + ") \\/ ";
        } else {
            result = result + String.valueOf(this.x) + " \\/ ";
        }
        if (this.y.precedence < precedence) {
            result = result + "(" + String.valueOf(this.x) + ")";
        } else {
            result = result + String.valueOf(this.y);
        }
        return result;
    }

    public Boolean eval(Map d) {
        return this.x.eval(d) || this.y.eval(d);
    }
}

class uppgift2c {
    public static void main(String[] args) {
        System.out.println(new Var("x"));
        System.out.println(new Const(false));
        System.out.println(new And(new Var("x"),new Var("y")));
        System.out.println(new Or(new Var("x"),new Var("y")));
        System.out.println(new Not(new Var("x")));
        System.out.println(new And(new Or(new Var("x"),new Var("y")),new Not(new Var("z"))));
        System.out.println(new Or(new Not(new Const(true)),new Var("x")));
        System.out.println(new Not(new And(new Var("x"),new Var("y"))));
        System.out.println(new And(new And(new Var("x"),new Var("y")),new Var("z")));
        System.out.println(new Or(new Or(new Var("x"),new Var("y")),new Var("z")));
        System.out.println(new Not(new Not(new Var("x"))));
        System.out.println(new Or(new Not(new Var("x")),new Var("x")));
        Map<String,Boolean> d1 = new HashMap<String,Boolean>();
        d1.put("x",false);
        System.out.println((new Or(new Not(new Var("x")),new Var("x"))).eval(d1));
        Map<String,Boolean> d2 = new HashMap<String,Boolean>();
        d2.put("x",false); d2.put("y",true); d2.put("z",true);
        System.out.println((new And(new And(new Var("x"),new Var("y")),new Var("z"))).eval(d2));
        Map<String,Boolean> d3 = new HashMap<String,Boolean>();
        d3.put("x",false); d3.put("y",true); d3.put("z",false);
        System.out.println((new And(new Or(new Var("x"),new Var("y")),new Not(new Var("z")))).eval(d3));
        System.out.println((new Var("x")).eval(d3));
        System.out.println((new Const(false)).eval(d3));
    }
}
