class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        target_index = 0

        for number in range(1, n + 1):
            result.append("Push")

            if number == target[target_index]:
                target_index += 1
                if target_index == len(target):
                    break
            else:
                result.append("Pop")

        return result

