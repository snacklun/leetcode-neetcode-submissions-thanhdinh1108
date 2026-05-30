public class Solution {
    public int MaxProfit(int[] prices) {
         int maxProfit = 0;
            int minPrice = int.MaxValue;
            foreach (var price in prices)
            {
                if (price < minPrice) minPrice = price;
                if (price - minPrice > maxProfit) maxProfit = price - minPrice;
            }
            return maxProfit;
    }
}
