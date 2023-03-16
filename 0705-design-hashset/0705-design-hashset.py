class MyHashSet:

    def __init__(self):
        self.myset=set()
        

    def add(self, key: int) -> None:
        self.myset.add(key)
        

    def remove(self, key: int) -> None:
        if self.contains(key)==False:
            return
        self.myset.remove(key)
        

    def contains(self, key: int) -> bool:
        if key in self.myset:
            return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)