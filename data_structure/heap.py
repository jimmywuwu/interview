class Heap:
    
    def __init__(self):
        self._list = [] 
    
    def insert(self, val):
        self._list.append(val)
        last_idx = len(self._list) - 1
        self._sift_up(last_idx)
    
    def pop(self):
        if not self._list:
            raise IndexError
        self._list[0], self._list[-1] = self._list[-1], self._list[0]
        element = self._list.pop()
        self._sift_down(0)
        return element
    
    def _sift_up(self, idx):
        while True:
            parent_idx = (idx - 1) // 2
            if self._list[idx] >= self._list[parent_idx]:
                break
            else:
                self._list[idx], self._list[parent_idx] =  self._list[parent_idx], self._list[idx]
                idx = parent_idx 

    def _sift_down(self, idx):
        # Check left and right
        end = len(self._list)
        while True:
            left_idx = 2*idx + 1
            right_idx = 2*idx + 2
            
            smallest_idx = idx
            
            # The smallest element must on the root
            if left_idx < end and self._list[left_idx] < self._list[smallest_idx]:
                smallest_idx = left_idx
            if right_idx < end and self._list[right_idx] < self._list[smallest_idx]:
                smallest_idx = right_idx
            if smallest_idx == idx:
                break
            
            # The swap the smallest and idx
            self._list[smallest_idx], self._list[idx] =  self._list[idx], self._list[smallest_idx]
            
            idx = smallest_idx

if __name__ == "__main__":
    """
    Heap 以array來實現全滿樹，可以讓記憶體排列較緊密

    主要功能分成兩個對外接口實現及兩個內部使用的function：
    1. pop: 將array首尾元素交換後，透過 _sift_down 自上而下將樹節點調整正確
    2. insert: 將新增元素 append在 array後，並透過 _sift_up，自下而上調整節點
    3. _sift_up: 全滿樹節點可以透過 (idx - 1)//2 方式找到該節點parent編號，不停向上swap 直到條件都滿足即可
    4. _sift_down: 全滿樹節點可以透過 2*idx +1, 2*idx+2 找到左節點、右節點編號，每一次迭代從當前節點、左節點、右節點中找尋最小元素，並與插入元素提換，不停替換直到所有路徑上都符合heap結構為止
    """
    heap = Heap()
    h = Heap()
    h.insert(1)
    h.insert(3)
    h.insert(100)
    h.insert(2)
    h.insert(10)
    h.insert(7)

    while h._list:
        print(h.pop())