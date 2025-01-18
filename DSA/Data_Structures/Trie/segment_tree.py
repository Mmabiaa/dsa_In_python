class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        self.build(data)

    def build(self, data):
        # Initialize leaves of segment tree
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        
        # Build tree by calculating parents
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index, value):
        index += self.n
        self.tree[index] = value
        
        # Update parents
        while index > 1:
            index //= 2
            self.tree[index] = self.tree[index * 2] + self.tree[index * 2 + 1]

    def query(self, left, right): 
        res = 0 
        left += self.n 
        right += self.n 
       
        while left < right: 
            if left & 1: 
                res += self.tree[left] 
                left += 1 
            if right & 1: 
                right -= 1 
                res += self.tree[right] 
            left //= 2 
            right //= 2 
            
        return res 

# Example usage
if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11]
    seg_tree = SegmentTree(data)
    
    print("Sum of values in range [1,4):", seg_tree.query(1,4)) # Outputs sum of elements at index [1,4) -> [3+5+7]
    
    seg_tree.update(1,10) # Update index 1 to value of `10`
    
    print("Sum of values in range [1,4) after update:", seg_tree.query(1,4)) # Outputs sum after update.
