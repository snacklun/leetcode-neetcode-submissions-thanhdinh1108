class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s2) < len(s1)):
            return False
        
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for char in s1:
            counter1[char] = counter1.setdefault(char, 0) +1

        l = 0
        r = len(s1)
        
        window_size = s2[:r]
        for char in window_size:
            counter2[char] = counter2.setdefault(char, 0) +1
        
        if (counter2 == counter1):
                return True

        for index in range(r,len(s2)):
            counter2[s2[l]] -= 1
            if counter2[s2[l]] == 0:
                counter2.pop(s2[l])
            counter2[s2[l + len(s1)]] += 1
            l += 1
            if (counter2 == counter1):
                return True

        if (counter2 == counter1):
                return True

        return False