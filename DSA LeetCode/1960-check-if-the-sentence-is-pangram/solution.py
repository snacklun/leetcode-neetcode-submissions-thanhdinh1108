class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        char_set = set()
        for index in range(len(sentence)):
            char_set.add(sentence[index])

        if len(char_set) == 26:
            return True
        else:
            return False
