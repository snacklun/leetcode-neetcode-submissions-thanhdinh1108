public class Solution {
    public int MaxProfit(int[] prices) {
        int result = 0;
        int l = 0;
        int r = 1;
        while (r < prices.Length)
        {
            if (prices[r] > prices[l])
            {
                int profit = prices[r] - prices[l];
                result = Math.Max(result, profit);
            }
            else
            {
                l = r;
            }

            r++;
        }

        return result;
    }
}
