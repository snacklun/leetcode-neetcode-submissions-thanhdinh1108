public class Solution {
    public int StrStr(string haystack, string needle) {
   // Edge case: if needle is empty, return 0 (by convention)
        if (needle.Length == 0)
            return 0;

        int hLen = haystack.Length;
        int nLen = needle.Length;

        // Loop through haystack
        for (int i = 0; i <= hLen - nLen; i++)
        {
            int j;
            // Check if substring starting at i matches needle
            for (j = 0; j < nLen; j++)
            {
                if (haystack[i + j] != needle[j])
                    break;
            }

            // If we reached end of needle, we found a match
            if (j == nLen)
                return i;
        }

        // If not found
        return -1;

    }
}
