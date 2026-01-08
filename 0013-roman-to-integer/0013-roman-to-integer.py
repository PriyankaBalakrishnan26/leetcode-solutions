class Solution:
    def romanToInt(self, s: str) -> int:
        dict_vals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        characters=list(s)
        total_value=0
        for i, j in enumerate(characters):
            if i < len(characters)-1:
                if j == 'C' and characters[i+1] in ['D', 'M'] :
                    total_value-=dict_vals[j]
                elif j == 'X' and characters[i+1] in ['L', 'C'] :
                    total_value-=dict_vals[j]
                elif j == 'I' and characters[i+1] in ['V', 'X'] :
                    total_value-=dict_vals[j]
                else:
                    total_value+=dict_vals[j]
            else:
                total_value+=dict_vals[j]

        return total_value
        