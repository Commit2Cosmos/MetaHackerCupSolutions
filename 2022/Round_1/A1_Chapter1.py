
class Solution:
    def process_input(self, file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            

        num_test_cases = int(lines[0].strip())
        index = 1
        
        for n in range(num_test_cases):
            N, K = map(int, lines[index].strip().split())
            index += 1

            arr1 = list(lines[index].strip().split())
            index += 1

            arr2 = list(lines[index].strip().split())
            index += 1

            res = self.solve(arr1, arr2, K, N)

            if res:
                self.add_output('outputs/A1.txt', f"Case #{n+1}: YES")
            else:
                self.add_output('outputs/A1.txt', f"Case #{n+1}: NO")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f"{to_write}\n")
            

    def solve(self, arr1, arr2, K, N) -> bool:

        if len(arr1) != len(arr2):
            return False
        
        arr_len = len(arr1)
        
        arr1 = arr1 + arr1

        for i in range(arr_len):
            if arr1[i] == arr2[0]:
                if not arr1[i:i+N] == arr2:
                    return False
                if K == 0:
                    return True if arr1[0] == arr2[0] else False
                if K == 1:
                    return True if arr1[0] != arr2[0] else False
                
                if arr_len == 2:
                    if (K % 2 == 0 and arr1[0] == arr2[0]) or (K % 2 == 1 and arr1[0] != arr2[0]):
                        return True
                    else:
                        return False

                return True

        return False


sol = Solution()
sol.process_input('./data/consecutive_cuts_chapter_1_input.txt')
