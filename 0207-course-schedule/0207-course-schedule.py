
class Solution:
    def DFT(self, v, visited, neighbor) -> None:        
        if neighbor[v] == []:
            return
        
        for i in neighbor[v] :
            if i in visited:
                return
            visited.add(i)
            self.DFT(i, visited, neighbor)
        return
    
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        neighbor = {}
        for v in range(numCourses):
            neighbor[v] = []
                
        for (v, w) in prerequisites:
            neighbor[v].append(w)
        
        for v in range(numCourses):
            visited=set()
            self.DFT(v, visited, neighbor)
            
            if v in visited:
                return False
            
        return True
                
