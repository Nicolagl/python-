class Array(object):
    def __init__(self,capacity,fillValue=None):
        self._items=list()
        for count in range(capacity):
            self._items.append(fillValue)
            
    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)
    
    def __iter__(self):
        return iter(self._items)
    def __getitem__(self,index):
        return self.__items[index]

    def __setitem__(self,index,newItem):
        self._items[index]=newItem


a=Array(5)
print(len(a),a)






'''class Grid(object):
    def __init__(self,rows,columns,fillValue=None):
        self._data=Array(rows)
        for row in range(rows):
            self._data[row]=Array(columns,fillValue)

tab=Grid(4,5,7)

print(tab)'''