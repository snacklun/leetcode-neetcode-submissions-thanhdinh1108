public class Solution {
    public bool IsAnagram(string s, string t) {
    if (s.Length != t.Length)
                {
                    return false;
                }

                var counts = new Dictionary<char, int>();
                foreach (var s_char in s)
                {
                    counts[s_char] = counts.GetValueOrDefault(s_char, 0) + 1;
                }
                
                foreach (var t_char in t)
                {
                    counts[t_char] = counts.GetValueOrDefault(t_char, 0) - 1;
                }

                foreach (var kvp in counts)
                {
                    if (kvp.Value != 0)
                        return false;
                }

                return true;
    }
}
