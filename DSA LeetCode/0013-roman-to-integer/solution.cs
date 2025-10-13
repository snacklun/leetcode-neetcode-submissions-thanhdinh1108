public class Solution {
    public int RomanToInt(string shmm) {
        var s = shmm.ToCharArray();
        var romanValues = new Dictionary<char, int>{
            { 'I', 1 },
            { 'V', 5 },
            { 'X', 10 },
            { 'L', 50 },
            { 'C', 100 },
            { 'D', 500 },
            { 'M', 1000 }
        };

        int result = 0;

        for (int i = 0; i < s.Length; i++)
        {
            if (i + 1 < s.Length)
            {
                if (s[i] == 'I' && s[i + 1] == 'V') { result += 4; i++; continue; }
                if (s[i] == 'I' && s[i + 1] == 'X') { result += 9; i++; continue; }
                if (s[i] == 'X' && s[i + 1] == 'L') { result += 40; i++; continue; }
                if (s[i] == 'X' && s[i + 1] == 'C') { result += 90; i++; continue; }
                if (s[i] == 'C' && s[i + 1] == 'D') { result += 400; i++; continue; }
                if (s[i] == 'C' && s[i + 1] == 'M') { result += 900; i++; continue; }
            }

            result += romanValues[s[i]];
        }

        return result;
    }
}

