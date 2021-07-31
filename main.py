# This is a sample Python script.

class smart_key(object):
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other):
        return (other.obj + self.obj) < (self.obj+other.obj)

join_to_bigges = lambda x: ''.join(sorted(map(str,x), key=smart_key))

print(join_to_bigges([5,2,1,8,9]))