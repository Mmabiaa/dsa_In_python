class DisjointSet:
    def __init__(self):
        self.parent = {}
    
    def find(self, item):
        if item not in self.parent:
            self.parent[item] = item
        
        if self.parent[item] != item:
            # Path compression optimization
            self.parent[item] = self.find(self.parent[item])
        
        return self.parent[item]

    def union(self, set_a, set_b):
        root_a = self.find(set_a)
        root_b = self.find(set_b)

        if root_a != root_b:
            self.parent[root_b] = root_a
            
# Example usage
if __name__ == "__main__":
    ds = DisjointSet()
    
    ds.union('A', 'B')
    ds.union('B', 'C')
    
    print(ds.find('A')) # Output: A (root of A's set)
    print(ds.find('C')) # Output: A (C is connected to A through B)
