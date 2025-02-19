class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):

            m = int(lines[index].strip())
            index += 1

            res = self.solve(m, lines[index].strip()[0])

            index += 1

            self.add_output('outputs/C1_SecondMeaning_output.txt', f"Case #{n+1}:")

            for r in res:
                self.add_output('outputs/C1_SecondMeaning_output.txt', f"{r}")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f'{to_write}\n')
            

    def solve(self, m: int, first_char: str) -> bool:
        
        res = ['-'*i + first_char if first_char == '.' else '.'*i + first_char for i in range(1, m)]
        
        return res


sol = Solution()
sol.process_input('./data/second_meaning_input.txt')