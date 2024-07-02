
class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            R, C = map(int, lines[index].strip().split())
            index += 1

            #* MAIN LOGIC GOES HERE

            res = self.solve()

            if res:
                self.add_output('outputs/___.txt', f"Case #{n+1}: YES")
            else:
                self.add_output('outputs/___.txt', f"Case #{n+1}: NO")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f"{to_write}\ n")
            
        
    @staticmethod
    def generate_symbols():
        pass


    def solve(self) -> bool:
        
        pass


sol = Solution()
sol.process_input('./data/___.txt')
