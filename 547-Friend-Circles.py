class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        N = len(M)
        roots = []
        for i in range(N):
            roots.append(i)
            
        def _find_root(p):
            root = roots[p]
            while root != roots[root]:
                root = roots[root]
            i = roots[p]
            while i != roots[i]:
                tmp = roots[i]
                roots[i] = root
                i = tmp
            return root
    
        
        def _union(p, q):
            root_p = _find_root(p)
            root_q = _find_root(q)
            roots[root_p] = root_q
            
        
        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    _union(i, j)
        cnt = 0
        for i in range(N):
            if roots[i] == i:
                cnt += 1
        
        return cnt