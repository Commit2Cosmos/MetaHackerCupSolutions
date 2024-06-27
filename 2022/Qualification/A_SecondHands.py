class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for i in range(num_test_cases):
            n, k = map(int, lines[index].strip().split())
            parts = list(map(int, lines[index + 1].strip().split()))
            index += 2

            if self.solve(n, k, parts):
                self.add_output('A_SecondHands_output.txt', f"Case #{i+1}: YES")
            else:
                self.add_output('A_SecondHands_output.txt', f"Case #{i+1}: NO")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f'{to_write}\n')
            
        
        
    @staticmethod
    def solve(n, k, parts) -> bool:
        
        if 2*k < n:
            return False
        
        
        s1, s2 = set(), set()

        for p in parts:
            if p in s1:
                if p in s2:
                    return False
                s2.add(p)
            else:
                s1.add(p)
        
        return True


sol = Solution()
sol.process_input('./data/second_hands_input.txt')