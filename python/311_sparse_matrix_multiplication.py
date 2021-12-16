class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        if not mat1 or not mat2 or not mat1[0] or not mat2[0]:
            return [[]]
       
        # m x k * k x n = m x n 
        
        m = len(mat1)
        n = len(mat2[0])
        k = len(mat1[0])
        
        output_mat = [[0 for _ in range(n)] for _ in range(m)]
        
        sparse_mat1 = self.get_tuple_repr(mat1)
        sparse_mat2 = self.get_tuple_repr(mat2)
        
        for i, j, v1 in sparse_mat1:
            for x, y, v2 in sparse_mat2:
                if j == x:
                    output_mat[i][y] += v1 * v2
        
        return output_mat
        
    
    def get_tuple_repr(self, mat):
        res = []
        m = len(mat)
        n = len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0:
                    res.append((i,j,mat[i][j]))
        
        return res