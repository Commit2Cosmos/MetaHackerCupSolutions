from typing import Union


class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            R, C = map(int, lines[index].strip().split())
            index += 1

            drawing = []
            
            for _ in range(R):
                drawing.append(list(lines[index].strip()))
                index += 1


            res = self.solve(R, C, drawing)

            if res:
                self.add_output('outputs/B1_SecondFriend_output.txt', f"Case #{n+1}: Possible")
                self.add_output('outputs/B1_SecondFriend_output.txt', f"{res}")
            else:
                self.add_output('outputs/B1_SecondFriend_output.txt', f"Case #{n+1}: Impossible")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f'{to_write}\n')
            
        
    @staticmethod
    def generate_symbols(rows, cols, symbol = '^'):
        return "\n".join([f'{symbol}' * cols] * rows)



    def solve(self, R, C, drawing) -> Union[str, None]:
        
        if R > 1 and C > 1:
            return self.generate_symbols(R, C)
        else:
            for i in drawing:
                for j in i:
                    if j == '^':
                        return None
            return self.generate_symbols(R, C, '.')


sol = Solution()
sol.process_input('./data/second_friend_input.txt')