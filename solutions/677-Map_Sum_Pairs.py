from collections import defaultdict

class MapSum:

    def __init__(self):
        self.my_map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        self.my_map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0

        for key, value in self.my_map.items():
            if prefix == key[:len(prefix)]:
                res += value
        
        return res

        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)