import math

class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            N, K, D = map(int, lines[index].strip().split())
            index += 1

            points = []

            for _ in range(N):
                x, y = map(int, lines[index].strip().split())
                points.append((x, y))
                index += 1
            
            res = self.solve(K, D, points)

            if res:
                self.add_output('outputs/c.txt', f"Case #{n+1}: {res}")


    @staticmethod
    def add_output(file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f"{to_write}\n")

    @staticmethod
    def polar_angle(p1, p2):
        return math.atan2(p1[0] - p2[0], p1[1] - p2[1])
    
    @staticmethod
    def distance(p1, p2):
        return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


    def sort_by_polar(self, points):
        pivot = points[0]
        return sorted(points, key=lambda p: (self.polar_angle(p, pivot), self.distance(p, pivot)))
    

    @staticmethod
    def cross_product(p1, p2, p3):
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    
    def dikstra(self, K, D, points, target) -> bool:
        
        V = len(points)
        dist = [float('inf')] * V
        dist[0] = 0
        visited = [False] * V
        prev = [None] * V

        target = points.index(target)


        def min_distance(dist, visited):
            min_val = float('inf')
            min_index = -1
            for v in range(V):
                if not visited[v] and dist[v] < min_val:
                    min_val = dist[v]
                    min_index = v
            return min_index
        

        for _ in range(V):

            u = min_distance(dist, visited)

            if u == -1:
                break

            visited[u] = True
            
            if u == target:
                break
            
            for v in range(V):
                d = self.distance(points[u], points[v])
                if d < D**2 and not visited[v] and dist[v] > dist[u] + max(d, K):
                    dist[v] = dist[u] + max(d, K)
                    prev[v] = u

        return dist[target] if dist[target] != float('inf') else -1


    def solve(self, K, D, points) -> bool:

        target = points[-1]
        
        #* find convex hull
        points = self.sort_by_polar(points)

        hull = []
        for p in points:
            while len(hull) >= 2 and self.cross_product(hull[-2], hull[-1], p) >= 0:
                hull.pop()
            hull.append(p)

        return self.dikstra(K, D, hull, target)


sol = Solution()
sol.process_input('./data/lemonade_life_input.txt')