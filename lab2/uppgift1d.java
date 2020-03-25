import java.util.List;
import java.util.ArrayList;

class IntegerSet {
    public List<Integer> set;
    public int cardinality;

    public IntegerSet() {
        set = new ArrayList<>();
        this.cardinality = 0;
    }

    public void insert(int e) {
        if (!this.set.contains(e)) {
            this.set.add(e);
            this.cardinality++;
        }
    }

    public boolean member(int e) {
        return this.set.contains(e);
    }

    public List<Integer> getMembers() {
        return this.set;
    }

    public int size() {
        return this.cardinality;
    }

    public String toString() {
        String result = "{";
        for (int e:this.set) {
            result = result + String.valueOf(e) + ",";
        }
        if (this.cardinality!=0) {
            result = result.substring(0, result.length() - 1);
        }
        return result + "}";
    }

    public void delete(int e) {
        if (this.set.contains(e)) {
            this.set.remove(new Integer(e));
            this.cardinality--;
        }
    }

    public boolean le(IntegerSet x) {
        for (int e:this.set) {
            if (!x.member(e)) {
                return false;
            }
        }
        return true;
    }

    public void union(IntegerSet x) {
        for (int e:x.getMembers()) {
            this.insert(e);
        }
    }

    public void intersect(IntegerSet x) {
        for (Integer e:new ArrayList<Integer>(this.set)) {
            if (!x.member(e)) {
                this.delete(e);
            }
        }
    }
}

class uppgift1d {
    public static void main(String[] args) {
        IntegerSet x = new IntegerSet();
        x.insert(2);
        x.insert(3);
        System.out.println(x);
        System.out.println(x.size());
        x.delete(2);
        System.out.println(x);
        System.out.println(x.size());
        x.delete(4);
        IntegerSet y = new IntegerSet();
        y.insert(3);
        y.insert(4);
        System.out.println(x.le(y));
        System.out.println(y.le(x));
        IntegerSet empty = new IntegerSet();
        System.out.println(x.le(empty));
        System.out.println(empty.le(x));
        x.union(y);
        System.out.println(x);
        x.intersect(empty);
        System.out.println(x);
        System.out.println(x.size());
        System.out.println(y);
        y.intersect(y);
        System.out.println(y);
        x.insert(3);
        y.intersect(x);
        System.out.println(y);
        System.out.println(y.size());
    }
}
