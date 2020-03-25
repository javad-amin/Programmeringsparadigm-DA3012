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
}
class uppgift1c {
    public static void main(String[] args) {
        IntegerSet x = new IntegerSet();
        System.out.println(x);
        System.out.println(x.size());
        x.insert(2);
        x.insert(3);
        x.insert(2);
        System.out.println(x);
        System.out.println(x.getMembers());
        System.out.println(x.size());
        System.out.println(x.member(4));
        System.out.println(x.member(2));
        for (int i=0; i<=10; i++) {
            x.insert(i);
        }
        System.out.println(x);
    }
}
