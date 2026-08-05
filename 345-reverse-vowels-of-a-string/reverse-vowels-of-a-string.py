class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = []
        out = ""
        for i in s:
            if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                vowel.append(i)
        position = len(vowel)-1
        for i in s:
            if i in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
                out += vowel[position]
                position -= 1
            else:
                out +=i
        return out
        