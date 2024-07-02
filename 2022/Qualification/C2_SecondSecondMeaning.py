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

            # print(res)

            index += 1

            self.add_output('outputs/C2_SecondMeaning_output.txt', f"Case #{n+1}:")

            for r in res:
                self.add_output('outputs/C2_SecondMeaning_output.txt', f"{r}")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f'{to_write}\n')
            

    def solve(self, m: int, first_char: str) -> bool:
        
        res = []
        to_append = '-' if first_char == '.' else '.'

        for i in range(1, m):

            binary_str = bin(i)[2:]
            binary_str = binary_str.zfill(9)
            binary_str = binary_str.replace('0', '.').replace('1', '-')

            res.append(to_append+binary_str)
        
        return res


sol = Solution()
sol.process_input('./data/second_second_meaning_input.txt')