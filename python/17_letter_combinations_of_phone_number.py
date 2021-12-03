class Solution:
    letter_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        def getCombos(index: int, path: List[str]):
            if len(path) == len(digits):
                combinations.append("".join(path))
                return
            
            for letter in self.letter_map[digits[index]]:

                path.append(letter)
                getCombos(index + 1, path)
                
                path.pop()
            
        combinations = []
        getCombos(0, [])
        return combinations