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


# x = IntegerSet()
# print(x)
# #{}
# print(x.size())
# #0
# x.insert(2)
# x.insert(3)
# x.insert(2)
# print(x)
# #{2,3}
# print(x.getMembers())
# #[2, 3]
# print(x.size())
# #2
# print(x.member(4))
# #False
# print(x.member(2))
# #True
# for i in range(10): x.insert(i)
# #...
# print(x)
# #{2,3,0,1,4,5,6,7,8,9}
