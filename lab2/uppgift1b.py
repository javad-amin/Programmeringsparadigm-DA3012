class IntegerSet:
    def __init__(self):
        self.set = []
        self.cardinality = 0

    def insert(self,e):
        if e not in self.set:
            self.set.append(e)
            self.cardinality += 1

    def member(self,e):
        return e in self.set

    def getMembers(self):
        return self.set

    def size(self):
        return self.cardinality

    def __str__(self):
        return '{' + ','.join(map(str, self.set)) + '}'

    def delete(self, e):
        if e in self.set:
            self.set.remove(e)
            self.cardinality -= 1
        else:
            raise ValueError("list.remove(x): x not in list")

    def __le__(self,x):
        for e in self.set:
            if not x.member(e):
                return False
        return True

    def union(self,x):
        for e in x.getMembers():
            self.insert(e)

    def intersect(self,x):
        for e in list(self.set):
                if not x.member(e):
                    self.delete(e)

    def intersection(self,x):  # :)
        for e in list(self.set):
                if not x.member(e):
                    self.delete(e)


# x = IntegerSet()
# x.insert(2)
# x.insert(3)
# print(x)
# #{2,3}
# print(x.size())
# #2
# x.delete(2)
# print(x)
# #{3}
# print(x.size())
# #1
# #x.delete(4)
# #Traceback (most recent call last):
# #...
# #ValueError: list.remove(x): x not in list
# y = IntegerSet()
# y.insert(3)
# y.insert(4)
# print(x <= y)
# #True
# print(y <= x)
# #False
# empty = IntegerSet()
# print(x <= empty)
# #False
# print(empty <= x)
# #True
# x.union(y)
# print(x)
# #{3,4}
# x.intersect(empty)
# print(x)
# #{}
# print(x.size())
# #0
# print(y)
# #{3,4}
# y.intersect(y)
# print(y)
# #{3,4}
# x.insert(3)
# y.intersect(x)
# print(y)
# #{3}
# print(y.size())
# #1
