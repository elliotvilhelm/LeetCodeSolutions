class SparseVector:
    def __init__(self, nums: List[int]):
        self.arr = nums
        
    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        sparse_vec = self.sparse_repr(vec)
        for i in range(len(self.arr)):
            if self.arr[i] != 0:
                if i in sparse_vec:
                    res += self.arr[i] * sparse_vec[i]
        return res
            
    def sparse_repr(self, sparse):
        res = {}
        arr = sparse.arr
        for i in range(len(arr)):
            if arr[i] != 0:
                res[i] = arr[i]
        return res
        

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)