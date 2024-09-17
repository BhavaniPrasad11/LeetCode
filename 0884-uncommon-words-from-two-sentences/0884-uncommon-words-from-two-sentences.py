class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        combined = s1.split() + s2.split()
        word_count = Counter(combined)
        result = [word for word in word_count if word_count[word] == 1]
        return result
