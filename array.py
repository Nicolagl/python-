class Array():
    def __init__(self,capacity,fillValue=None):
        self._items=list()
        for count in range(capacity):
            self._items.append(fillValue)
            
    def __len__(self):
        return len(self._items)

a=Array(5)
print(len(a),a)