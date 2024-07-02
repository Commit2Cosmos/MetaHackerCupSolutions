
class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            N = int(lines[index].strip())
            index += 1

            trees_X = []
            trees_Y = []

            for _ in range(N):
                X, Y = map(int, lines[index].strip().split())
                trees_X.append(X)
                trees_Y.append(Y)
                index += 1

            Q = int(lines[index].strip())
            index += 1

            wells_X = []
            wells_Y = []

            for _ in range(Q):
                X, Y = map(int, lines[index].strip().split())
                wells_X.append(X)
                wells_Y.append(Y)
                index += 1

            res = self.solve(trees_X, trees_Y, wells_X, wells_Y, N, Q)

            if res:
                self.add_output('outputs/b2.txt', f"Case #{n+1}: {res}")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f"{to_write}\n")


    def solve(self, trees_X, trees_Y, wells_X, wells_Y, N, Q) -> bool:
        MOD = 1000000007

        tree_x = tree_y = tree_x_sq = tree_y_sq = 0

        for n in range(N):
            tree_x = (tree_x + trees_X[n]) % MOD
            tree_x_sq = (tree_x_sq + trees_X[n]**2) % MOD
            
            tree_y = (tree_y + trees_Y[n]) % MOD
            tree_y_sq = (tree_y_sq + trees_Y[n]**2) % MOD

        res = 0

        for q in range(Q):
            res = (res + N*wells_X[q]**2 - 2*tree_x*wells_X[q] + tree_x_sq) % MOD
            res = (res + N*wells_Y[q]**2 - 2*tree_y*wells_Y[q] + tree_y_sq) % MOD

        return res



sol = Solution()
sol.process_input('./data/watering_well_chapter_2_input.txt')
