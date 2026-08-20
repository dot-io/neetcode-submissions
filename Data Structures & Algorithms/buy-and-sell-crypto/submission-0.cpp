class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int max_profit = 0;
        for (int i = 0; i < prices.size(); i++) {
            int sell_price = prices[i];
            for (int j = 0; j < i; j++) {
                int buy_price = prices[j];
                if (sell_price - buy_price > max_profit) {
                    max_profit = sell_price - buy_price;
                }
            }
        }
        return max_profit;
    }
};
