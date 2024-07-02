
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
                self.add_output('outputs/A2.txt', f"Case #{n+1}: YES")
            else:
                self.add_output('outputs/A2.txt', f"Case #{n+1}: NO")


    def add_output(self, file_path, to_write):
        with open(file_path, 'a') as file:
            file.write(f"{to_write}\n")
            
    
    @staticmethod
    def kmp(haystack, needle):
        lps = [0] * len(needle)

        prevLPS, i = 0, 1

        #* setting up lps
        while i < len(needle):
            if needle[i] == needle[prevLPS]:
                lps[i] = prevLPS + 1
                prevLPS += 1
                i += 1
            
            elif prevLPS == 0:
                lps[i] = 0
                i += 1
            
            else:
                prevLPS = lps[prevLPS - 1]

        
        i, j = 0, 0

        while i < len(haystack):
            if haystack[i] == needle[j]:
                i, j = i+1, j+1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j-1]
            
            if j == len(needle):
                return i - len(needle)
        
        return None 




    def solve(self, arr1, arr2, K, N) -> bool:

        if len(arr1) != len(arr2):
            return False
        
        arr1 = arr1 + arr1

        res = None

        #* find first time occurrence of arr2 in arr1
        if K == 1:
            res = self.kmp(arr1[1:-1], arr2)
            
        else:
            res = self.kmp(arr1, arr2)

        if res is not None:
            
            if K == 0:
                return True if res == 0 else False
            
            if N == 2:
                if (K % 2 == 0 and arr1[0] == arr2[0]) or (K % 2 == 1 and arr1[0] != arr2[0]) or (arr1[0] == arr1[1] == arr2[0] == arr2[1]):
                    return True
                else:
                    return False

            return True

        return False


sol = Solution()
sol.process_input('./data/consecutive_cuts_chapter_2_input.txt')

# print(sol.kmp(haystack=[1, 1000000000, 1, 1, 1000000000, 1], needle=[1, 1, 1000000000]))