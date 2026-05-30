public class Solution {
    public int MaxProfit(int[] prices) {
        int max = 0;
            for (int i = 0; i < prices.Length; i++)
            {
                for (int j = i + 1; j < prices.Length; j++)
                {
                    if (prices[j] > prices[i])
                    {
                        var profit = prices[j] - prices[i];
                        if (profit > max) { max = profit; }

                    }
                }

            }
            return max;
    }
}
