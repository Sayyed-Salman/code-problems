class ValidAnagram:

    def __init__(self, s: str, t: str) -> None:
        self.s = s
        self.t = t

    def check_valid_anagram(self) -> bool:

        if len(self.s) != len(self.t):
            return False

        countS, countT = {}, {}
        for c in range(len(self.s)):
            countS[self.s[c]] = countS.get(self.s[c], 0) + 1
            countT[self.t[c]] = countT.get(self.t[c], 0) + 1

        return countS == countT


s = "salman"
t = "sayyed"
anagram = ValidAnagram(s, t)
result = anagram.check_valid_anagram()
if result:
    print(f"String {s} and {t} are anagrams")
else:
    print(f"String {s} and {t} are not anagrams")
