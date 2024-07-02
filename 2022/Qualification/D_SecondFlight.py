from collections import defaultdict


class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            _, M, Q = map(int, lines[index].strip().split())
            index += 1

            adj_lst = defaultdict(dict)

            for _ in range(M):
                X, Y, P = map(int, lines[index].strip().split())
                adj_lst[X][Y] = adj_lst[Y][X] = P
                index += 1


            #* 1. Hash table (map) -> adjacency list
            #* 2. Check if direct connection exists -> add to total
            #* 3. Check if any connections have a connection with destination

            self.add_output('outputs/D_SecondFlight_output.txt', f"Case #{n+1}:")

            for _ in range(Q):
                X, Y = map(int, lines[index].strip().split())
                res = self.solve(X, Y, adj_lst)
                self.add_output('outputs/D_SecondFlight_output.txt', f" {res}")
                index += 1


            self.add_output('outputs/D_SecondFlight_output.txt', f"\n")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f'{to_write}')

    def solve(self, X, Y, adj_lst) -> int:
        
        tot = 0

        for connection in adj_lst[X]:
            if connection == Y:
                tot += 2 * adj_lst[X][connection]

            if connection in adj_lst[Y]:
                tot += min(adj_lst[X][connection], adj_lst[Y][connection])

        return tot
            


sol = Solution()
sol.process_input('./data/second_flight_test_input.txt')